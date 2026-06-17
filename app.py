from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_input = input("Ask Anything that's troubling you...\n> ")

response_instructions = "You are a decision-making assistant, you help people to come out of complex situations by providing them with solutions responding with pros, cons, blindspots user might be missing and an advice. Help the user handle the situation optimally."

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = user_input,
    config = genai.types.GenerateContentConfig(
        system_instruction = response_instructions,
        response_mime_type = "application/json")
)

with open("./response.json", 'w') as response_file:
    response_file.write(response.text)

print("Done!")
