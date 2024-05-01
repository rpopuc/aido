import os
import ollama
from lib.api_provider import APIProvider

class OllamaProvider(APIProvider):
    def get_default_model(self):
        return os.getenv('OLLAM_DEFAULT_MODEL') or 'codegemma'

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

