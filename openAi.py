import openai
from dotenv import load_dotenv
import os

load_dotenv()


class OpenAiClient:
    def __init__(self):
        openai.api_key = os.environ['OPENAI_API_KEY']

    async def ask_gpt(self, message):
        try:
            # Send a prompt to OpenAI and get a response using the updated API
            response = openai.chat.completions.create(
                model="gpt-4",  # Use an appropriate model
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error: {e}")
            return "I'm having trouble processing that request."
