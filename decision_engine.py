from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response_instructions = "You are a decision-making assistant/ strategist, you help people to come out of complex situations by providing them with solutions responding with pros, cons, blindspots user might be missing and advice. Help the user handle the situation optimally, make something out of their messy thoughts."


def get_response(question):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = question,
        config = genai.types.GenerateContentConfig(
            system_instruction = response_instructions,
            response_mime_type = "application/json")
    )

    return json.loads(response.text)
