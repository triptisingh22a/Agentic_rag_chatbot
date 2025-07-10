import os
from core.file_processor import extract_text, chunk_text

class IngestionAgent:
    def __init__(self):
        # Ensure the uploaded_files directory exists
        os.makedirs("uploaded_files", exist_ok=True)

    def process(self, uploaded_files, query, trace_id="trace-1"):
        documents = []
        for file in uploaded_files:
            # Extract file extension to determine file type
            file_type = os.path.splitext(file.name)[1].lower().lstrip('.')

            # Create a unique path for each file inside uploaded_files/
            file_path = os.path.join("uploaded_files", file.name)

            # Save uploaded file to disk
            with open(file_path, "wb") as f:
                f.write(file.read())

            # Extract text content from file
            try:
                content = extract_text(file_path, file_type)
            except Exception as e:
                raise ValueError(f"Failed to process file '{file.name}': {e}")

            # Chunk the content
            chunks = chunk_text(content)
            documents.extend(chunks)

        return {
    "trace_id": trace_id,
    "payload": {
        "query": query,
        "chunks": documents  # <- this must match what retrieval_agent expects
    }
}

