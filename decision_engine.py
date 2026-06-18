from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
import json

# Parsing API Key Securely
load_dotenv()

client = genai.Client()

model = "gemini-3.1-flash-lite"
# model = "gemini-2.5-flash",

# Response Schema for JSON output
class ResponseFormat(BaseModel):
    pros: list[str]
    cons: list[str]
    blind_spot: str
    advice: str
    confidence_score: int

response_instructions = "You are a decision-making assistant/ strategist, you help people to come out of complex situations by providing them with solutions responding with pros, cons, blindspots user might be missing and advice. Help the user handle the situation optimally, make something out of their messy thoughts. Also give a confidence score on your suggestion on a scale of 1 to 10"

# Main funcition: sends user input and fetches the response
def get_response(question):
    response = client.models.generate_content(
        model = model,
        contents = question,
        config = genai.types.GenerateContentConfig(
            system_instruction = response_instructions,
            response_mime_type = "application/json",
            response_schema=ResponseFormat)
    )

    # Conversion of plain string response into JSON object
    return json.loads(response.text)
