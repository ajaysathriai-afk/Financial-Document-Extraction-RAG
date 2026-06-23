from app.rag import answer_question

questions = [
    "What were Apple's total liabilities in 2024?",
    "What was shareholder equity in 2024?",
    "What cash balance did Apple end fiscal 2024 with?",
    "How much cash was used in financing activities?",
    "What were total net sales in fiscal year 2024?"
]

for q in questions:

    print("\n" + "="*60)
    print(q)
    print("="*60)

    answer = answer_question(q)

    print(answer)