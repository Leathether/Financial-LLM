import os
from dotenv import load_dotenv
import mypy
from embeddings import vector


load_dotenv()

from groq import Groq

client = Groq(
    api_key = os.environ.get("GROQ_API_KEY")

)


chat_completion = client.chat.completions.create(
    messages=[{
        "role": "user",
        "message": "Name a ticker symbol that will go up soon: ex: 'TSLA'",
    }],
    model="llama-3.3-70b-versatile",
    embeddings=vector,
)

llm = chat_completion.choices[0].message.content

print(llm)