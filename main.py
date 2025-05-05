import os
import requests
import json
from typing import List
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display, update_display
from openai import OpenAI
import ollama

MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key)>10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key? Please visit the troubleshooting notebook!")

openai = OpenAI()

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

system_prompt = """
You are a helpful chatbot that answers questions about code
"""

# gpt-4o-mini
def gpt_bot():
    stream = openai.chat.completions.create(
        model=MODEL_GPT,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        stream=True
    )

    response = ""
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ''
        response += delta
        print(delta, end='', flush=True)

if __name__ == "__main__":
    print("\n🤖 gpt-4o-mini is thinking...\n")
    gpt_bot()

###############################################################

## Llama 3.2
# def llama_bot():
#     response = ollama.chat(
#         model=MODEL_LLAMA,
#         messages=[
#             {"role": "system", "content": system_prompt},
#             {"role": "user", "content": question}
#         ],
#         stream=True
#     )

#     full_response = ""
#     for chunk in response:
#         if 'message' in chunk and 'content' in chunk['message']:
#             content = chunk['message']['content']
#             print(content, end='', flush=True)
#             full_response += content

#     return full_response


# if __name__ == "__main__":
#     print("\n🤖 LLaMA is thinking...\n")
#     llama_bot()