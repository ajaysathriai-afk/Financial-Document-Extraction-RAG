from app.pdf_parser import extract_text_from_pdf
from app.extractor import extract_financial_sections
from app.rag import store_sections

text = extract_text_from_pdf(
    "sample_docs/apple_2024_10k.pdf"
)

sections = extract_financial_sections(text)

count = store_sections(sections)

print(
    f"Stored {count} sections"
)