from app.rag import search_documents

results = search_documents(
    "What was Apple's revenue in 2024?"
)

for i, doc in enumerate(results):

    print(f"\n--- RESULT {i+1} ---\n")
    print(doc[:1000])
