import os
import anthropic
from lib.api_provider import APIProvider

class AnthropicProvider(APIProvider):
    def get_default_model(self):
        return os.getenv('ANTHROPIC_DEFAULT_MODEL') or "claude-3-haiku-20240307"

    def get_response(self, prompt):
        client = anthropic.Anthropic()

        message = client.messages.create(
            model=self.model,
            max_tokens=1000,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": "R:"
                        }
                    ]
                }
            ]
        )
        return message.content[0].text
