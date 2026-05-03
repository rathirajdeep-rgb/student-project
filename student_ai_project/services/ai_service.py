import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

def ask_ai(question):
    response = client.chat.completions.create(model = "gpt-4o-mini",
     messages = [{"role": "system", "content": "You are a helpful student data assistant."},
                {"role": "user", "content": question}
                ]
    )
    return response.choices[0].message.content
