import os
import ollama
from lib.api_provider import APIProvider

class OllamaProvider(APIProvider):
    def get_default_model(self):
        return os.getenv('OLLAMA_DEFAULT_MODEL') or 'olmo2'

    def get_response(self, prompt):
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                },
                {
                    "role": "assistant",
                    "content": "R:"
                }
            ]
        )
        return response['message']['content']

