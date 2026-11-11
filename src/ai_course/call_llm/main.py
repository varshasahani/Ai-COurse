import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()  # Load environment variables from .env file
class ChatServices:
    def __init__(self):
        api_key=os.environ.get("openrouterapikey")
        self.client = AsyncOpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")

    async def chat(self, prompt):
        response = await self.client.chat.completions.create(
            model="nvidia/nemotron-3-ultra-550b-a55b:free",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

async def main():
    chat_service = ChatServices()
    prompt = input("Enter your prompt: ")
    response = await chat_service.chat(prompt)
    print("Response from the model:", response)

if __name__ == "__main__":
    asyncio.run(main())