# Financial Document Extraction & RAG Platform

AI-powered Financial Document Extraction and Retrieval-Augmented Generation (RAG) platform built using GPT-4o, OpenAI Embeddings, ChromaDB, FastAPI, Docker, PostgreSQL, and AWS.

---

## 🌐 Live Demo

### Frontend

http://financial-rag-frontend-ajay.s3-website.ap-south-1.amazonaws.com

### Backend API

http://13.235.115.168:8000

### API Documentation

http://13.235.115.168:8000/docs

---

# 📸 Application Demo

![Financial RAG Demo](screenshots/demo.png)

---

# 📖 Project Overview

This platform automates extraction of key financial metrics from annual reports (10-K PDFs) and enables intelligent financial question answering using Retrieval-Augmented Generation (RAG).

### Core Capabilities

* Upload Financial Reports
* Extract Financial Metrics using GPT-4o
* Validate Structured Output
* Generate Confidence Scores
* Create OpenAI Embeddings
* Store Vectors in ChromaDB
* Perform Semantic Search
* Ask Natural Language Questions
* Receive Context-Aware Answers

---

# 🏗️ Architecture Diagram

```mermaid
flowchart TD

A[Frontend UI]
    |
    v

B[FastAPI Backend]
    |
    v

C[PDF Parser]
    |
    v

D[Chunking Engine]
    |
    v

E[Financial Section Detection]

E --> F[GPT-4o Extraction]

F --> G[Validation Layer]

G --> H[Confidence Scoring]

H --> I[(PostgreSQL)]

E --> J[Section Extraction]

J --> K[OpenAI Embeddings]

K --> L[(ChromaDB)]

L --> M[RAG Retrieval]

M --> N[GPT-4o Answer Generation]

N --> O[Question Answering API]
```

---

# 🔄 End-to-End Workflow

```mermaid
flowchart TD

A[Upload Financial Report]
    |
    v

B[Parse PDF]
    |
    v

C[Chunk Document]
    |
    v

D[Detect Financial Sections]

D --> E[GPT-4o Financial Extraction]

E --> F[Validate Output]

F --> G[Confidence Scoring]

G --> H[Return Financial Metrics]

D --> I[Extract Financial Sections]

I --> J[Generate OpenAI Embeddings]

J --> K[Store in ChromaDB]

K --> L[User Asks Question]

L --> M[Semantic Retrieval]

M --> N[GPT-4o Answer Generation]

N --> O[Display Final Answer]
```

---

# ☁️ Deployment Architecture

```mermaid
flowchart TD

A[User]
    |
    v

B[AWS S3 Static Website]
    |
    v

C[Frontend UI]
    |
    v

D[AWS EC2 Instance]
    |
    v

E[Docker Container]
    |
    v

F[FastAPI Backend]

F --> G[GPT-4o]

F --> H[OpenAI Embeddings]

H --> I[(ChromaDB)]

F --> J[(PostgreSQL)]
```

---

# 🚀 Features

## Financial Extraction

* PDF Parsing
* Intelligent Chunking
* Financial Statement Detection
* GPT-4o Structured Extraction
* Validation Layer
* Confidence Scoring

## Retrieval-Augmented Generation (RAG)

* OpenAI Embeddings
* ChromaDB Vector Search
* Semantic Retrieval
* Context-Aware Responses
* GPT-4o Question Answering

## Cloud Deployment

* Dockerized Backend
* AWS EC2 Deployment
* AWS S3 Frontend Hosting
* Public REST APIs
* Production Ready

---

# 🛠️ Technology Stack

| Layer            | Technology                    |
| ---------------- | ----------------------------- |
| Frontend         | HTML, CSS, JavaScript         |
| Backend          | FastAPI                       |
| LLM              | GPT-4o                        |
| Embeddings       | OpenAI text-embedding-3-small |
| Vector Database  | ChromaDB                      |
| Database         | PostgreSQL                    |
| Containerization | Docker                        |
| Cloud            | AWS EC2                       |
| Static Hosting   | AWS S3                        |
| CI/CD            | GitHub Actions                |

---

# 📂 Project Structure

```text
Financial-Document-Extraction-RAG
│
├── app/
│   ├── main.py
│   ├── extractor.py
│   ├── rag.py
│   ├── pdf_parser.py
│   ├── validator.py
│   ├── confidence.py
│   └── repository.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── screenshots/
│   └── demo.png
│
├── tests/
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 📊 Example Financial Metrics

The platform extracts:

* Revenue
* Gross Margin
* Operating Income
* Net Income
* Total Assets
* Total Liabilities
* Shareholders Equity
* Cash & Cash Equivalents

Example:

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
  "confidence_score": 1,
  "review_required": false
}
```

---

# 💬 Sample Questions

```text
What was Apple's revenue in 2024?

What were Apple's total liabilities?

What was shareholder equity in 2024?

How much cash was used in financing activities?

What cash balance did Apple end fiscal 2024 with?

What was Apple's operating income in fiscal year 2024?
```

---

# 🔮 Future Enhancements

* Multi-Document Analysis
* Multi-Company Comparison
* Financial Trend Analysis
* Interactive Dashboards
* Advanced RAG Strategies
* Financial Ratio Calculations
* Production Monitoring

---

# 👨‍💻 Author

**Ajay Kumar Sathri**

MS in Computer Science Engineering
University of North Texas

GitHub:
https://github.com/ajaysathriai-afk

---

# ✅ Project Status

* Financial Extraction Working
* GPT-4o Integrated
* OpenAI Embeddings Integrated
* ChromaDB Working
* RAG Pipeline Working
* Dockerized
* AWS EC2 Deployed
* AWS S3 Hosted
* End-to-End Tested
* Portfolio Ready

```
```
