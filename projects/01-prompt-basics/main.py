import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """You are an assistant that extracts structured data from messy real estate lead messages. Always respond ONLY in valid JSON with these fields: name, phone, property_interest, budget, timeline. If a field isn't mentioned, use null."""

user_message = "hi im sarah, interested in the downtown condo, no idea on budget yet, call me at 555-2201"
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
)

print(response.choices[0].message.content)