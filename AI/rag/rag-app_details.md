These are Python package dependencies commonly used for building an **AI/LLM application**, especially a **RAG (Retrieval-Augmented Generation)** or document-based chatbot system.

Let’s explain each one in simple interview-ready terms 👇

---

# 🧩 Dependency List Overview

```txt
fastapi>=0.110.0
uvicorn[standard]>=0.29.0
chromadb>=0.5.0
sentence-transformers>=3.0.0
pypdf>=4.0.0
python-docx>=1.1.0
requests>=2.31.0
python-multipart>=0.0.9
```

These packages together help:

* Build APIs
* Run web servers
* Process PDFs/DOCX files
* Generate embeddings
* Store vectors
* Upload documents
* Connect external APIs

---

# 🔹 1. FastAPI

```txt
fastapi>=0.110.0
```

## ➤ What it is:

A modern, high-performance Python web framework used to build APIs quickly.

## ➤ Why used in AI/LLM apps:

Used to expose AI services as REST APIs.

Example:

```python
POST /chat
POST /upload
GET /search
```

## ➤ Features:

* Very fast (async support)
* Auto-generates Swagger/OpenAPI docs
* Easy integration with AI models

## ➤ Use Cases:

* Chatbot backend
* RAG API service
* AI microservices

---

# 🔹 2. Uvicorn

```txt
uvicorn[standard]>=0.29.0
```

## ➤ What it is:

A lightweight ASGI server used to run FastAPI applications.

## ➤ Simple understanding:

If FastAPI is the application, Uvicorn is the engine/server that runs it.

## ➤ Example:

```bash
uvicorn main:app --reload
```

## ➤ `[standard]` means:

Install extra performance dependencies:

* websockets
* uvloop
* httptools

## ➤ Use Cases:

* Running AI APIs
* Async request handling
* Real-time streaming/chat

---

# 🔹 3. ChromaDB

```txt
chromadb>=0.5.0
```

## ➤ What it is:

An open-source vector database for storing embeddings.

## ➤ Why important in AI:

Used in RAG systems to:

* Store document embeddings
* Perform semantic similarity search

## ➤ Example:

User asks:

> “What is leave policy?”

ChromaDB finds semantically similar chunks from uploaded documents.

## ➤ Core Features:

* Vector storage
* Similarity search
* Metadata filtering

## ➤ Common AI Use:

* Enterprise knowledge chatbot
* Semantic search
* AI copilots

---

# 🔹 4. Sentence Transformers

```txt
sentence-transformers>=3.0.0
```

## ➤ What it is:

A library for generating embeddings from text using transformer models.

Built on top of:

* BERT
* RoBERTa
* MiniLM
* MPNet

## ➤ What it does:

Converts text into vectors.

Example:

```python
"The server is down"
→ [0.21, -0.44, 0.77, ...]
```

## ➤ Used for:

* Semantic search
* Vectorization
* Similarity matching

## ➤ Popular Models:

* all-MiniLM-L6-v2
* mpnet-base-v2

---

# 🔹 5. PyPDF

```txt
pypdf>=4.0.0
```

## ➤ What it is:

Python library for reading and extracting text from PDF files.

## ➤ AI Use Cases:

Used in document ingestion pipelines.

Example:

```python
Extract text from HR_Policy.pdf
```

## ➤ Common Operations:

* Read PDFs
* Extract pages/text
* Merge/split PDFs

---

# 🔹 6. python-docx

```txt
python-docx>=1.1.0
```

## ➤ What it is:

Library for reading and writing Microsoft Word `.docx` files.

## ➤ AI Use Cases:

Extract enterprise documents into text for embeddings/vectorization.

Example:

```python
Read SOP.docx
Extract paragraphs
```

## ➤ Used in:

* RAG ingestion pipelines
* Enterprise document processing

---

# 🔹 7. Requests

```txt
requests>=2.31.0
```

## ➤ What it is:

Most popular Python library for making HTTP/API calls.

## ➤ AI Use Cases:

Used to call:

* OpenAI APIs
* OCI GenAI APIs
* External enterprise APIs

## ➤ Example:

```python
requests.post("https://api.openai.com/v1/chat/completions")
```

## ➤ Used for:

* REST integrations
* External services
* API orchestration

---

# 🔹 8. python-multipart

```txt
python-multipart>=0.0.9
```

## ➤ What it is:

Library used by FastAPI to handle file uploads.

## ➤ Example:

Uploading:

* PDFs
* DOCX files
* Images

through:

```http
multipart/form-data
```

## ➤ Required for:

```python
UploadFile = File(...)
```

## ➤ AI Use Cases:

Document upload for RAG/chatbot systems.

---

# 🏗️ Overall Architecture Flow

```text
User Uploads PDF/DOCX
        ↓
FastAPI API
        ↓
PyPDF / python-docx extract text
        ↓
Sentence Transformers create embeddings
        ↓
ChromaDB stores vectors
        ↓
User asks question
        ↓
Similarity search in ChromaDB
        ↓
LLM generates response
        ↓
Uvicorn serves API
```

---

# 🧠 Interview-Ready One-Line Summary

| Package               | Simple Interview Explanation          |
| --------------------- | ------------------------------------- |
| FastAPI               | Python framework for building AI APIs |
| Uvicorn               | ASGI server to run FastAPI apps       |
| ChromaDB              | Vector database for semantic search   |
| Sentence Transformers | Creates embeddings from text          |
| PyPDF                 | Extracts text from PDFs               |
| python-docx           | Reads Word documents                  |
| Requests              | Makes HTTP/API calls                  |
| python-multipart      | Supports file uploads in FastAPI      |



