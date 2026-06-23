from app.prompts import EXTRACTION_PROMPT

def chunk_text(text: str, chunk_size: int = 5000):
    """
    Split large text into smaller chunks.
    """
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def find_financial_chunks(chunks):

    important_sections = [
        "CONSOLIDATED STATEMENTS OF OPERATIONS",
        "CONSOLIDATED BALANCE SHEETS",
        "CONSOLIDATED STATEMENTS OF CASH FLOWS"
    ]

    relevant_chunks = []

    for idx, chunk in enumerate(chunks):

        chunk_upper = chunk.upper()

        for section in important_sections:

            if section in chunk_upper:
                relevant_chunks.append((idx, chunk))
                break

    return relevant_chunks

import re

def extract_financial_sections(text):

    sections = {}

    patterns = {
        "operations":
        r"CONSOLIDATED STATEMENTS OF OPERATIONS",

        "balance_sheet":
        r"CONSOLIDATED BALANCE SHEETS",

        "cash_flow":
        r"CONSOLIDATED STATEMENTS OF CASH FLOWS"
    }

    for section_name, pattern in patterns.items():

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            start = match.start()

            sections[section_name] = text[
                start:start + 12000
            ]

    return sections








from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def extract_financial_metrics(chunk):

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": EXTRACTION_PROMPT
            },
            {
                "role": "user",
                "content": chunk
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content
