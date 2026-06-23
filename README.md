# Financial Document Extraction & RAG Platform

An AI-powered platform that automatically extracts key financial metrics from annual reports (10-K PDFs) and enables natural language question answering using Retrieval-Augmented Generation (RAG).

The system combines Large Language Models (GPT-4o), OpenAI Embeddings, ChromaDB Vector Search, and FastAPI to transform unstructured financial reports into an interactive financial intelligence platform.

---

## Project Overview

Financial reports often contain hundreds of pages of complex financial statements and disclosures. Manually searching for important metrics such as revenue, net income, liabilities, shareholder equity, or cash flow can be time-consuming.

This platform automates the process by:

- Uploading annual reports (PDF)
- Extracting financial metrics using GPT-4o
- Detecting key financial statements
- Generating vector embeddings
- Storing financial knowledge in ChromaDB
- Answering natural language questions using RAG

---

## Key Features

### Financial Metric Extraction

Automatically extracts:

- Revenue
- Gross Margin
- Operating Income
- Net Income
- Total Assets
- Total Liabilities
- Shareholders Equity
- Cash & Cash Equivalents

---

### AI-Powered Question Answering

Ask questions such as:

```text
What was Apple's revenue in 2024?

What were total liabilities in 2024?

What was shareholder equity?

How much cash was used in financing activities?
```

and receive contextual answers directly from the uploaded report.

---

### Retrieval Augmented Generation (RAG)

The platform:

1. Detects important financial sections
2. Creates vector embeddings
3. Stores them in ChromaDB
4. Retrieves relevant context
5. Uses GPT-4o to generate accurate answers

---

### Confidence Scoring

Each extraction includes:

- Confidence Score
- Review Flag
- Validation Layer

to improve reliability and data quality.

---

## Architecture

```text
┌──────────────────────────┐
│      User Browser        │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ AWS S3 Static Frontend   │
│ HTML + CSS + JavaScript  │
└────────────┬─────────────┘
             │ REST API
             ▼
┌──────────────────────────┐
│ FastAPI Backend (EC2)    │
│ Docker Container         │
└────────────┬─────────────┘
             │
             ▼
      PDF Upload
             │
             ▼
┌──────────────────────────┐
│ PyMuPDF Parser           │
│ PDF Text Extraction      │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ Financial Statement      │
│ Detection Engine         │
└────────────┬─────────────┘
             │
             ├──────────────► GPT-4o
             │                Financial
             │                Metric Extraction
             │
             ▼
┌──────────────────────────┐
│ Financial Sections       │
│ Operations              │
│ Balance Sheet           │
│ Cash Flow               │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ OpenAI Embeddings        │
│ text-embedding-3-small   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ ChromaDB Vector Store    │
│ Semantic Search          │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ GPT-4o RAG Engine        │
│ Question Answering       │
└──────────────────────────┘
```

---

## End-to-End Workflow

```text
PDF Upload
    ↓
PDF Parsing
    ↓
Financial Statement Detection
    ↓
GPT-4o Metric Extraction
    ↓
Schema Validation
    ↓
Confidence Scoring
    ↓
OpenAI Embeddings
    ↓
ChromaDB Vector Storage
    ↓
Natural Language Questions
    ↓
Semantic Retrieval
    ↓
GPT-4o Response Generation
```

---

## Technology Stack

### Frontend

- HTML
- CSS
- JavaScript
- AWS S3 Static Website Hosting

### Backend

- Python
- FastAPI

### AI & LLM

- GPT-4o
- OpenAI API
- Prompt Engineering

### Vector Database

- ChromaDB

### Embeddings

- OpenAI text-embedding-3-small

### Document Processing

- PyMuPDF

### Deployment

- Docker
- AWS EC2
- AWS S3

---

## Demo Screenshot

> Upload a screenshot of the complete workflow and save it as:

```text
screenshots/demo.png
```

Then GitHub will render it automatically:

![Financial RAG Demo](screenshots/demo.png)

---

## Example Extraction Output

```json
{
  "company_name": "Apple Inc.",
  "fiscal_year": 2024,
  "revenue": 391035,
  "gross_margin": 180683,
  "operating_income": 123216,
  "net_income": 93736,
  "total_assets": 364980,
  "total_liabilities": 308030,
  "shareholders_equity": 56950,
  "cash_and_cash_equivalents": 29943,
  "confidence_score": 1.0
}
```

---

## Example Questions

```text
What was Apple's revenue in 2024?

What were total liabilities in 2024?

What was shareholder equity in 2024?

How much cash was used in financing activities?

What was Apple's net income?
```

---

## Project Highlights

- End-to-End AI Application
- Financial Document Intelligence
- Retrieval Augmented Generation (RAG)
- OpenAI Embeddings
- Vector Search
- GPT-4o Integration
- FastAPI REST APIs
- Dockerized Deployment
- AWS Cloud Deployment
- Production Ready Architecture

---

## Future Enhancements

- Multi-Document Support
- Multi-Company Analysis
- Financial Trend Visualization
- Historical KPI Comparisons
- Pinecone Vector Database
- User Authentication
- Role-Based Access Control
- Advanced Analytics Dashboard

---

## Deployment

### Backend

AWS EC2 + Docker

### Frontend

AWS S3 Static Website Hosting

### AI Services

OpenAI GPT-4o + OpenAI Embeddings

### Vector Database

ChromaDB

---

## Author

**Ajay Kumar Sathri**

AI / ML Engineer | Generative AI Developer | Full Stack Engineer

Built as part of an end-to-end Generative AI portfolio focused on:

- LLM Applications
- Retrieval Augmented Generation
- AI Agents
- Cloud-Native AI Systems
- Production AI Deployment