from app.pdf_parser import extract_text_from_pdf
from app.extractor import (
    chunk_text,
    find_financial_chunks,
    extract_financial_metrics
)

text = extract_text_from_pdf(
    "sample_docs/apple_2024_10k.pdf"
)

print("Text Length:", len(text))

chunks = chunk_text(text)

print("Chunks:", len(chunks))

financial_chunks = find_financial_chunks(chunks)

print("Financial Chunks:", len(financial_chunks))

result = extract_financial_metrics(
    financial_chunks[0][1]
)

print(result)
