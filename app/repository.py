from app.database import SessionLocal
from app.models import FinancialMetricsDB


def save_financial_metrics(data):

    db = SessionLocal()

    record = FinancialMetricsDB(
        company_name=data["company_name"],
        fiscal_year=data["fiscal_year"],
        revenue=data["revenue"],
        gross_margin=data["gross_margin"],
        operating_income=data["operating_income"],
        net_income=data["net_income"],
        confidence_score=data["confidence_score"],
        review_required=data["review_required"]
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    db.close()

    return record.id
