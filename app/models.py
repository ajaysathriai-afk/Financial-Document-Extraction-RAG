from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Boolean
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FinancialMetricsDB(Base):

    __tablename__ = "financial_metrics"

    id = Column(Integer, primary_key=True)

    company_name = Column(String)

    fiscal_year = Column(Integer)

    revenue = Column(Float)

    gross_margin = Column(Float)

    operating_income = Column(Float)

    net_income = Column(Float)

    confidence_score = Column(Float)

    review_required = Column(Boolean)
