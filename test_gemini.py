# File: test_gemini.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

# Create model and generate content
try:
    # Use the recommended model from the docs
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Write a story about a magic backpack.")
    print("Success! Here's the response:\n")
    print(response.text)
except Exception as e:
    print(f"Error occurred: {str(e)}")