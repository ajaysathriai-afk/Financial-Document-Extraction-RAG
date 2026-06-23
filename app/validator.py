from app.schemas import FinancialMetrics

def validate_extraction(data: dict):

    try:
        validated = FinancialMetrics(**data)
        return validated

    except Exception as e:

        print(f"Validation Error: {e}")
        return None