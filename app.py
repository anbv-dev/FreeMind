from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_input = input("Ask Anything...\n> ")

response_instructions = '''\nReturn the response in a structured mannner in pure json format covering different aspects/parameters: {"pros": [...], "cons": [...], "blindspot": "...", "advice": "..."}. \nHelp the user to handle the situation in most optimal way. '''

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = user_input + response_instructions
    )

print("Done!")
