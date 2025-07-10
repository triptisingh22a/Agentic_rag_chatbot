# Agentic_rag_chatbot

An agentic Retrieval-Augmented Generation (RAG) chatbot that integrates the power of LLMs with external document retrieval to answer queries intelligently. Designed for tasks requiring domain-specific knowledge and multi-step reasoning.

---

## 🚀 Features

- 🔍 **Retrieval-Augmented Generation** using vector search
- 🧠 **LLM-powered responses** grounded in relevant documents
- 🗂️ **Custom document loaders** for PDFs, web pages, and more
- 🛠️ **Agentic architecture** for chaining tools & logic
- ⚙️ Built with Python, LangChain, and HuggingFace/LLM APIs

---

## 🧰 Tech Stack

- Python 3.10+
- LangChain
- FAISS / ChromaDB
- OpenAI / Llama2 / Ollama (plug-and-play)
- Streamlit / Gradio (optional UI)
- PyPDF, BeautifulSoup, etc. (for document parsing)

---

## 📦 Installation

```bash
git clone https://github.com/triptisingh22a/Agentic_rag_chatbot.git
cd Agentic_RAG_Bot
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
