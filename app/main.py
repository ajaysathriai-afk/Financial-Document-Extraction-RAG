from pydantic import BaseModel
from app.rag import (
    answer_question,
    store_sections
)

from fastapi.middleware.cors import CORSMiddleware
from fastapi import (
    FastAPI,
    UploadFile,
    File
)

import json
import os

from app.validator import validate_extraction
from app.pdf_parser import extract_text_from_pdf
from app.repository import save_financial_metrics

from app.extractor import (
    chunk_text,
    find_financial_chunks,
    extract_financial_metrics,
    extract_financial_sections
)

app = FastAPI(
    title="Financial Document Extraction API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def health():
    return {
        "status": "healthy",
        "service": "financial-document-extraction"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    answer = answer_question(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }


@app.post("/extract")
async def extract_document(
    file: UploadFile = File(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # STEP 1: PDF PARSE

    text = extract_text_from_pdf(
        file_path
    )

    # STEP 2: STORE RAG SECTIONS

    sections = extract_financial_sections(
        text
    )

    if sections:
        store_sections(sections)

    # STEP 3: CHUNKING

    chunks = chunk_text(text)

    # STEP 4: FIND FINANCIAL CHUNKS

    financial_chunks = find_financial_chunks(
        chunks
    )

    if not financial_chunks:
        return {
            "error": "No financial sections found"
        }

    # STEP 5: GPT EXTRACTION

    combined_context = "\n\n".join(
        chunk[1]
        for chunk in financial_chunks
    )

    result = extract_financial_metrics(
        combined_context
    )

    try:

        cleaned = (
            result
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        data = json.loads(cleaned)

        from app.confidence import (
            calculate_confidence
        )

        confidence = calculate_confidence(
            data
        )

        data["confidence_score"] = confidence
        data["review_required"] = (
            confidence < 0.80
        )

        validated = validate_extraction(
            data
        )

        if validated is None:

            return {
                "status": "validation_failed",
                "message": "Pydantic schema validation failed"
            }

        response = validated.model_dump()

        response["record_id"] = 1

        return response

    except Exception as e:

        return {
            "error": str(e),
            "raw_response": result
        }