import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ] 
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        
        response = get_openai_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()