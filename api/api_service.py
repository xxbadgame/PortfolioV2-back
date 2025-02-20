import requests
from mistralai import Mistral
from django.conf import settings

class ApiService:
    def __init__(self):
        self.api_key = settings.MISTRAL_API_KEY
        self.client = Mistral(api_key=self.api_key)

    def get_chat_response(self, agent_id, message):
        response = self.client.agents.complete(
            agent_id=agent_id,
            messages=[
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )
        return response.choices[0].message.content