from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def main():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role" : "system", "content": "You are a helpful assistant"},
            {"role": "assistant", "content": "My name is Alexander"},
            {"role": "assistant", "content": "My surname is Kazimirsky"},
            {"role" : "user", "content": "What is your surname?"}
        ])
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()