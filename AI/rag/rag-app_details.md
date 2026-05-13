# Tools
- Antigravity
- Claude Sonnet 4.6
- React
- Phython
- Node.js
- fastapi>=0.110.0
- uvicorn[standard]>=0.29.0
- chromadb>=0.5.0
- sentence-transformers>=3.0.0
- pypdf>=4.0.0
- python-docx>=1.1.0
- requests>=2.31.0
- python-multipart>=0.0.9
- Ollama
  - Deepseek-deepseek-coder
  - Google-gemma4:8b
  - Qwen-qwen2.5
  - Qwen-qwen3.5:4b
  - Microsoft-phi3
  - Meta-llama3
  - TheBloke-mistral

# RAG Chatbot — Quick Start


## Prerequisites
- Python 3.10+
- Node.js 18+
- [Ollama](https://ollama.com) running locally with a model pulled

## 1. Pull an Ollama model (if not done)
```
ollama pull llama3.2
```

## 2. Start the backend
```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## 3. Start the frontend
```
cd frontend
npm install
npm run dev
```

## 4. Open the app
Visit: http://localhost:5173

## Usage
1. Upload a PDF/TXT/DOCX in the left sidebar
2. Wait for indexing to complete
3. Ask questions — the AI will cite sources from your documents


==================


# Frontend

These are core technologies commonly used to build a modern **frontend web application**, especially for AI dashboards, copilots, chatbots, admin portals, and enterprise applications.

Let’s explain each one clearly and interview-ready 👇

---

# 🧩 Frontend Technology Stack Overview

```txt id="vqby7p"
react
react-dom
lucide-react
node
npm
vite.config.js
```

Together, they help developers:

* Build UI components
* Render web pages
* Use icons
* Manage packages
* Run development servers
* Configure frontend builds

---

# 🔹 1. React

## ➤ What it is:

A popular JavaScript library for building modern user interfaces (UI), created by Meta.

## ➤ Main Idea:

UI is built using reusable **components**.

Example:

```jsx id="h94m59"
function Button() {
  return <button>Submit</button>
}
```

---

## ➤ Key Features:

* Component-based architecture
* Virtual DOM for fast rendering
* State management
* Reactive UI updates

---

## ➤ Common Use Cases:

* AI chatbot UI
* Dashboards
* Enterprise portals
* Single Page Applications (SPA)

---

## ➤ In AI Applications:

Used to create:

* Chat interfaces
* Document upload screens
* AI copilots
* Analytics dashboards

---

# 🔹 2. React DOM

## ➤ What it is:

A package that connects React components to the browser DOM.

## ➤ Simple Understanding:

* React creates components
* ReactDOM renders them into HTML/webpage

Example:

```jsx id="5r4igk"
ReactDOM.createRoot(document.getElementById('root')).render(<App />)
```

---

## ➤ Role:

Acts as the bridge between:

```text id="7v5jtx"
React Components → Browser DOM
```

---

# 🔹 3. Lucide (`lucide-react`)

## ➤ What it is:

A lightweight modern icon library for React applications.

## ➤ Why Used:

Provides clean SVG icons.

Example:

```jsx id="hsp7h2"
import { Search } from "lucide-react"

<Search />
```

---

## ➤ Common Icons:

* Search
* Upload
* Settings
* User
* Bot
* Menu

---

## ➤ AI Application Use Cases:

* Chatbot icons
* Upload buttons
* Navigation menus
* AI assistant indicators

---

# 🔹 4. Node.js

## ➤ What it is:

A JavaScript runtime environment that allows JavaScript to run outside the browser.

## ➤ Why Important:

Frontend tools like React/Vite/npm require Node.js.

---

## ➤ Common Uses:

* Running development servers
* Installing packages
* Backend APIs
* Build tooling

---

## ➤ Example:

```bash id="b4du2q"
node app.js
```

---

## ➤ In React Projects:

Node.js powers:

* npm
* Vite
* Webpack
* Build systems

---

# 🔹 5. npm

## ➤ What it is:

The default package manager for Node.js.

## ➤ Purpose:

Used to install/manage frontend dependencies.

Example:

```bash id="q83qlf"
npm install react
```

---

## ➤ Common Commands:

| Command         | Purpose                  |
| --------------- | ------------------------ |
| `npm install`   | Install dependencies     |
| `npm run dev`   | Start development server |
| `npm run build` | Build production app     |

---

## ➤ Role in AI Apps:

Installs:

* React
* Tailwind CSS
* Chat UI libraries
* AI SDKs

---

# 🔹 6. `vite.config.js`

## ➤ What it is:

Configuration file for Vite.

## ➤ What is Vite?

A modern frontend build tool and development server for React/Vue/etc.

Much faster than older tools like Webpack.

---

## ➤ Purpose of `vite.config.js`

Used to configure:

* Build settings
* Aliases
* API proxies
* Environment variables
* Plugins

---

## ➤ Example:

```js id="nrt9kn"
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    port: 3000
  }
})
```

---

## ➤ Common AI Use Cases:

Proxy frontend requests to FastAPI backend:

```text id="zftjfc"
React Frontend → FastAPI Backend
```

---

# 🏗️ How These Work Together

```text id="4o6n5j"
React Components
       ↓
ReactDOM renders UI
       ↓
Lucide icons improve UI
       ↓
npm installs dependencies
       ↓
Node.js runs tooling/dev server
       ↓
Vite builds and serves app
       ↓
Frontend connects to AI backend APIs
```

---

# 🧠 Real AI Chatbot Frontend Example

## Components:

| Technology | Role                           |
| ---------- | ------------------------------ |
| React      | Build chatbot UI               |
| ReactDOM   | Render UI                      |
| Lucide     | Chat/send/upload icons         |
| Node.js    | Runtime environment            |
| npm        | Dependency management          |
| Vite       | Fast frontend build/dev server |

---

# 🔹 Example Architecture

```text id="r3vm1m"
React Frontend (Vite)
       ↓
FastAPI Backend
       ↓
LLM APIs / Vector DB
```

---

# 🧠 Interview-Ready One-Line Explanations

| Technology     | Simple Interview Explanation                              |
| -------------- | --------------------------------------------------------- |
| React          | Component-based frontend library for building dynamic UIs |
| ReactDOM       | Renders React components into browser DOM                 |
| lucide-react   | Modern React SVG icon library                             |
| Node.js        | JavaScript runtime used for frontend/backend tooling      |
| npm            | Package manager for installing JavaScript dependencies    |
| vite.config.js | Configuration file for Vite frontend build tool           |


=========================

# Backend

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



