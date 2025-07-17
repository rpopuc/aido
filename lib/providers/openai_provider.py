import os
import openai
from lib.api_provider import APIProvider

class OpenAIProvider(APIProvider):
    def get_default_model(self):
        return os.getenv('OPENAI_DEFAULT_MODEL') or 'gpt-3.5-turbo'

    def get_response(self, prompt):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        response = openai.chat.completions.create(
            model=self.model,
            temperature=0,
            max_tokens=150,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
