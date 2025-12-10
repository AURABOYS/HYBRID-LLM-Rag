import requests

class LocalMistral:
    def __init__(self, model: str = "mistral:latest", host: str = "http://localhost:11434"):
        self.model = model
        self.host = host.rstrip("/")

    def answer(self, prompt: str):
        """
        Call local Ollama (Mistral) and return plain text.
        We use stream=false so that the response is a single JSON object.
        """
        url = f"{self.host}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,  # 👈 IMPORTANT: disable streaming to avoid JSONDecodeError
        }

        r = requests.post(url, json=payload, timeout=120)
        r.raise_for_status()

        data = r.json()
        # Ollama returns the generated text in "response"
        return {"response": data.get("response", "")}
