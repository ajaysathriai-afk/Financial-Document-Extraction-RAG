-- documents table

CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    document_name VARCHAR(255),
    upload_time TIMESTAMP,
    status VARCHAR(50)
);

-- financial_metrics table

CREATE TABLE financial_metrics (
    id SERIAL PRIMARY KEY,
    document_id INT,
    revenue FLOAT,
    gross_margin FLOAT,
    operating_income FLOAT,
    net_income FLOAT,
    confidence_score FLOAT,
    review_required BOOLEAN
);

-- audit_logs table

CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    document_id INT,
    raw_llm_output TEXT,
    created_at TIMESTAMP
);
