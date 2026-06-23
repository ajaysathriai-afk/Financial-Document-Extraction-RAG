from pydantic import BaseModel
from app.rag import answer_question

from fastapi import (
    FastAPI,
    UploadFile,
    File
)
import json
from app.validator import validate_extraction
from app.pdf_parser import extract_text_from_pdf
from app.repository import save_financial_metrics
from app.extractor import (
    chunk_text,
    find_financial_chunks,
    extract_financial_metrics
)

app = FastAPI(
    title="Financial Document Extraction API"
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
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    # Step 1: Parse PDF
    text = extract_text_from_pdf(file_path)

    # Step 2: Chunking
    chunks = chunk_text(text)

    # Step 3: Financial Section Detection
    financial_chunks = find_financial_chunks(chunks)

    if not financial_chunks:
        return {
            "error": "No financial sections found"
        }

    # Step 4: GPT Extraction
    result = extract_financial_metrics(
        financial_chunks[0][1]
    )

    try:

        cleaned = (
            result
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        data = json.loads(cleaned)
        from app.confidence import calculate_confidence

        confidence = calculate_confidence(data)

        data["confidence_score"] = confidence
        data["review_required"] = confidence < 0.80

        validated = validate_extraction(data)

        if validated is None:
            return {
                "status": "validation_failed",
                "message": "Pydantic schema validation failed"
            }
        
        record_id = save_financial_metrics(
            validated.model_dump()
        )

        response = validated.model_dump()
        response["record_id"] = record_id

        return response

    except Exception as e:

        return {
            "error": str(e),
            "raw_response": result
        }
