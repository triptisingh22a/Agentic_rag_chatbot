from core.vector_store import store_chunks, retrieve_top_k
from core.mcp import create_message

class RetrievalAgent:
    def process(self, message: dict) -> str:
        try:
            query = message["payload"]["query"]
            context_chunks = message["payload"]["chunks"]
        except KeyError as e:
            raise Exception(f"Missing key in message payload: {e}")
        
        if not isinstance(query, str):
            raise TypeError(f"Expected 'query' to be a string but got {type(query)}")
        
        self.vector_store = store_chunks(context_chunks)
        top_chunks = retrieve_top_k(self.vector_store, query, k=5)
        return "\n".join(top_chunks)
