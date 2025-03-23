import os
from groq import Groq

LLM_KEY = "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"


class GroqChatClient:
    def __init__(self, api_key: str = None):
        """Initialize the Groq client with an API key."""
        self.client = Groq(api_key=LLM_KEY)

    def chat(self, message: str, model: str = "gemma2-9b-it") -> str:
        """Send a message to the Groq chat model and return the response."""
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": message}],
            model=model,
        )
        return response.choices[0].message.content

# Usage example
if __name__ == "__main__":
    groq_client = GroqChatClient()
    response = groq_client.chat("Explain the importance of fast language models")
    print(response)
