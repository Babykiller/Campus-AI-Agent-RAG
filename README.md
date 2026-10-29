# Campus AI Agent (RAG-Based)

An end-to-end Retrieval-Augmented Generation (RAG) assistant designed for campus knowledge retrieval, such as exam schedules and course information. The system indexes local text data into a vector database and generates grounded answers using a Large Language Model.

## Core Features

- **Local Vector Database**: Utilizes ChromaDB for persistent local storage and efficient Top-K semantic search.
- **Context-Aware Retrieval**: Uses the `BAAI/bge-small-zh-v1.5` embedding model to convert text into high-dimensional vectors for accurate retrieval.
- **Hallucination Mitigation**: Enforces strict prompt templates to ensure the LLM generates answers solely based on retrieved context.
- **Conversational Memory**: Maintains short-term dialogue history via Streamlit's Session State.

## Tech Stack

- **Language**: Python 3.13+
- **Frontend**: Streamlit
- **Vector Database**: ChromaDB
- **Embedding Model**: BAAI/bge-small-zh-v1.5 (via `sentence-transformers`)
- **LLM Integration**: DeepSeek API (via OpenAI SDK)

## Project Structure

```text
├── app.py               # Streamlit application entry point
├── chroma_demo.py       # Script to generate and persist the vector database
├── knowledge.txt        # Source knowledge base (plain text)
└── chroma_db/           # Local persistent vector database directory

Getting Started
Clone the repository and navigate to the project directory.
git clone https://github.com/Babykiller/Campus-AI-Agent-RAG.git
cd Campus-AI-Agent-RAG
