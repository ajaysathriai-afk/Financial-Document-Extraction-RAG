from dotenv import load_dotenv

load_dotenv()

import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="financial_documents"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def store_sections(sections):

    documents = []
    ids = []
    metadatas = []

    for section_name, content in sections.items():

        documents.append(content)

        ids.append(section_name)

        metadatas.append(
            {
                "section": section_name
            }
        )

    embeddings = model.encode(documents)

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings.tolist()
    )

    return len(documents)



def search_documents(query):

    target_section = detect_section(query)

    query_embedding = model.encode([query])[0]

    if target_section:

        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=1,
            where={
                "section": target_section
            }
        )

    else:

        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=1
        )

    return results["documents"][0]

from openai import OpenAI
import os

def get_openai_client():
    return OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

def answer_question(question):

    docs = search_documents(question)

    context = "\n\n".join(docs)
    client_openai = get_openai_client()
    response = client_openai.chat.completions.create(
        model="gpt-4o",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": """
                Answer ONLY using the provided context.
                If information is missing say:
                'Information not found in document.'
                """
            },
            {
                "role": "user",
                "content": f"""
                Context:

                {context}

                Question:
                {question}
                """
            }
        ]
    )

    return response.choices[0].message.content

def detect_section(question):

    question = question.lower()

    operations_keywords = [
        "revenue",
        "sales",
        "net sales",
        "gross margin",
        "operating income",
        "net income",
        "earnings"
    ]

    balance_keywords = [
        "asset",
        "assets",
        "liabilities",
        "equity",
        "shareholders equity",
        "cash balance"
    ]

    cashflow_keywords = [
        "cash flow",
        "cash flows",
        "operating cash",
        "financing",
        "investing activities"
    ]

    for word in operations_keywords:
        if word in question:
            return "operations"

    for word in balance_keywords:
        if word in question:
            return "balance_sheet"

    for word in cashflow_keywords:
        if word in question:
            return "cash_flow"

    return None