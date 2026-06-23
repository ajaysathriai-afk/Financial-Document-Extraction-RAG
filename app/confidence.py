def calculate_confidence(data: dict):

    score = 0.0

    required_fields = [
        "company_name",
        "fiscal_year",
        "revenue",
        "gross_margin",
        "operating_income",
        "net_income"
    ]

    # Required fields present
    present = sum(
        1 for field in required_fields
        if data.get(field) not in [None, "", 0]
    )

    score += (present / len(required_fields)) * 0.6

    # Financial fields extracted
    financial_fields = [
        "revenue",
        "gross_margin",
        "operating_income",
        "net_income"
    ]

    extracted = sum(
        1 for field in financial_fields
        if data.get(field, 0) > 0
    )

    score += (extracted / len(financial_fields)) * 0.4

    return round(score, 2)
