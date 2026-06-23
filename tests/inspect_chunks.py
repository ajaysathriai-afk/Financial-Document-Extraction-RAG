from app.pdf_parser import extract_text_from_pdf
from app.extractor import chunk_text

text = extract_text_from_pdf(
    "sample_docs/apple_2024_10k.pdf"
)

chunks = chunk_text(text)

for i, chunk in enumerate(chunks):

    if "CONSOLIDATED" in chunk.upper():

        print("\n====================")
        print("CHUNK:", i)
        print("====================")

        print(chunk[:1500])
