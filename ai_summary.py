from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def summarize(news_text):

    prompt = f"""
You are a news assistant.

Summarize the following news into three sections:

1. Sports
2. Politics
3. AI

Use short bullet points.
Keep the entire message under 1000 characters.

News:

{news_text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content