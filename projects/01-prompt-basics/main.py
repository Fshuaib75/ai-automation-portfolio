import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """You are an assistant that extracts structured data from messy real estate lead messages. Always respond ONLY in valid JSON with these fields: name, phone, property_interest, budget, timeline. If a field isn't mentioned, use null.

IMPORTANT: Only extract information about the PRIMARY sender/lead (the person writing the message), not other people they mention (like family members, friends, or referrals). If the message mentions someone else's details, ignore those and only capture the sender's own info.

Examples:

Input: "hi its sarah, my sister sara jones might also want a house around 700k, my number is 555-1122, im looking to buy around 350k"
Output: {"name": "sarah", "phone": "555-1122", "property_interest": null, "budget": "350k", "timeline": null}

Input: "hey its dave again following up on the 300k place, my brother might also be looking to buy something around 500-600k too, his number is 555-9012"
Output: {"name": "dave", "phone": null, "property_interest": "300k place", "budget": "300k", "timeline": null}
"""

user_message = "hey its dave again following up on the 300k place, my brother might also be looking to buy something around 500-600k too, his number is 555-9012"
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
)

print(response.choices[0].message.content)