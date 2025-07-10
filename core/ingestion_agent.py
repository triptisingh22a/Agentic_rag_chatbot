from core.doc_parser import parse_document
from core.mcp import create_message

class IngestionAgent:
    def process(self, files, trace_id):
        all_chunks = []
        for file in files:
            parsed = parse_document(file)
            all_chunks.extend(parsed)
        return create_message("IngestionAgent", "RetrievalAgent", "PARSED_CHUNKS", trace_id, {
            "chunks": all_chunks
        })
