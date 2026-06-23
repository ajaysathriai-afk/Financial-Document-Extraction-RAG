from app.pdf_parser import extract_text_from_pdf
from app.extractor import chunk_text, find_financial_chunks

text = extract_text_from_pdf(
    "sample_docs/apple_2024_10k.pdf"
)

chunks = chunk_text(text)

financial_chunks = find_financial_chunks(chunks)

print("Sections Found:", len(financial_chunks))

for idx, chunk in financial_chunks:
    print("\n----------------")
    print("Chunk:", idx)
    print(chunk[:300])
