from pydantic import BaseModel, Field


class FinancialMetrics(BaseModel):
    company_name: str
    fiscal_year: int

    revenue: float
    gross_margin: float
    operating_income: float
    net_income: float

    total_assets: float
    total_liabilities: float
    shareholders_equity: float

    cash_and_cash_equivalents: float

    confidence_score: float = Field(
        ge=0.0,
        le=1.0
    )

    review_required: bool = False