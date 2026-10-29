Campus AI Agent (RAG-Based)
An end-to-end Retrieval-Augmented Generation (RAG) assistant designed for campus knowledge retrieval, such as exam schedules and course information. The system indexes local text data into a vector database and generates grounded answers using a Large Language Model.

Core Features
Local Vector Database: Utilizes ChromaDB for persistent local storage and efficient Top-K semantic search.

Context-Aware Retrieval: Uses the BAAI/bge-small-zh-v1.5 embedding model to convert text into high-dimensional vectors for accurate retrieval.

Hallucination Mitigation: Enforces strict prompt templates to ensure the LLM generates answers solely based on retrieved context.

Conversational Memory: Maintains short-term dialogue history via Streamlit's Session State.

Tech Stack
Language: Python 3.13+

Frontend: Streamlit

Vector Database: ChromaDB

Embedding Model: BAAI/bge-small-zh-v1.5 (via sentence-transformers)

LLM Integration: DeepSeek API (via OpenAI SDK)

Project Structure
```bash
├── app.py               # Streamlit application entry point
├── chroma_demo.py       # Script to generate and persist the vector database
├── knowledge.txt        # Source knowledge base (plain text)
└── chroma_db/           # Local persistent vector database directory
```
Getting Started
1.Clone the repository and navigate to the project directory.
```bash
git clone https://github.com/Babykiller/Campus-AI-Agent-RAG.git
cd Campus-AI-Agent-RAG
```
2.Install dependencies.
```bash
pip install -r requirements.txt
```
3.Build the vector database.
```bash
python chroma_demo.py
```
4.Run the application.
```bash
streamlit run app.py
```
Engineering Challenges & Solutions
1. HuggingFace Network Timeout
Issue: Model loading stalled during initialization due to connection blocks to huggingface.co.
Solution: Configured HF_ENDPOINT to use a domestic mirror and enabled HF_HUB_OFFLINE mode during Streamlit runtime to prevent redundant network requests.

2. Windows Symlink Limitations
Issue: huggingface_hub issued warnings about symlink failures on Windows.
Solution: Relied on the local cache mechanism rather than symlinks, accepting a minor increase in disk usage to ensure model files load correctly.

3. Path Parsing on Windows
Issue: Special characters in the Windows username path caused import failures.
Solution: Standardized on relative paths and proper string encoding throughout the codebase.
