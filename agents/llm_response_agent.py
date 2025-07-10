import requests

class LLMResponseAgent:
    def __init__(self, model: str = 'mistral'):
        self.model = model
        self.base_url = "http://localhost:11434/api/generate"

    def process(self, context: str, query: str) -> str:
        """
        Sends context and query to the local Ollama server and returns the response.
        """
        full_prompt = f"""You are a helpful assistant. Use the following context to answer the question.

        ### Context:
        {context}

        ### Question:
        {query}

        ### Answer:"""

        payload = {
            "model": self.model,
            "prompt": full_prompt,
            "stream": False
        }

        try:
            print(f"\n📤 Sending prompt to Ollama:\n{payload}\n")
            response = requests.post(self.base_url, json=payload)
            print(f"\n📥 Ollama raw response: {response.status_code} - {response.text}\n")
            response.raise_for_status()
            data = response.json()
            return data.get("response", "").strip()

        except requests.exceptions.RequestException as e:
            raise Exception(f"❌ Error communicating with Ollama: {e}")

        except KeyError:
            raise Exception(f"❌ Unexpected response format from Ollama: {response.text}")
