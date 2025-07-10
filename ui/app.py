import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from main import Coordinator

st.title("📄 Multi-Format Agentic RAG Chatbot")

uploaded_files = st.file_uploader("Upload your documents", type=["pdf", "docx", "pptx", "csv", "txt", "md"], accept_multiple_files=True)
query = st.text_input("Ask a question")

if st.button("Submit"):
    if uploaded_files and query:
        coordinator = Coordinator()
        response = coordinator.handle(uploaded_files, query)

        st.markdown("### ✅ Answer")
        st.write(response["payload"]["answer"])

        st.markdown("### 📚 Source Context")
        st.write(response["payload"]["source"])
    else:
        st.error("Please upload files and enter a question.")
