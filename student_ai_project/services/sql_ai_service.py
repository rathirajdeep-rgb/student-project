import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

def generate_sql(question):
    prompt = f"""
You are a SQL expert.

Convert the user question into a valid MYSQL query.

Table name: student_predictions
columns:
- age
- study_hours
- sleep_hours
- attendance
- marks
- result

Rules:
- only generate select queries
- Do not explain anything
- Do not add comments
- return only SQL query

Question: {question}
"""
    response = client.chat.completions.create(model = 'gpt-4o-mini', messages = [{"role": "system", "content": "You generate SQL query only."},
                                                                                {"role": "user", "content": prompt}
        ]
    )
    content = response.choices[0].message.content.strip()
    # Remove markdown code blocks if present
    if content.startswith("```"):
        lines = content.split('\n')
        if lines and (lines[0].startswith("```sql") or lines[0] == "```"):
            content = '\n'.join(lines[1:])
        if content.endswith("```"):
            content = content[:-3].strip()
    return content
