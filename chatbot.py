from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in .env file.")
genai.configure(api_key=api_key)

# Load the model
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("🤖 Gemini Chatbot (type 'exit' to quit)")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bye! 👋")
            break
        response = chat.send_message(user_input)
        print("Gemini:", response.text)
    except Exception as e:
        print("Error:", e)
