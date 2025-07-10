import uuid
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent

class Coordinator:
    def __init__(self):
        self.ingest = IngestionAgent()
        self.retrieve = RetrievalAgent()
        self.llm = LLMResponseAgent()

    def handle(self, uploaded_files, query):
        # Generate a unique trace/session ID
        trace_id = str(uuid.uuid4())

        # Step 1: Ingest documents
        parsed_msg = self.ingest.process(uploaded_files, query)


        # Step 2: Retrieve relevant chunks
        retrieval_msg = self.retrieve.process(parsed_msg)

        # Guard against empty retrieval results
        if not retrieval_msg.strip():
            raise ValueError("⚠️ Retrieval message is empty. Nothing to send to LLM.")

        # Step 3: Run through LLM to generate response
        return self.llm.process(retrieval_msg, query)
