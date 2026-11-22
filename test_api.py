import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # load environment variables

openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key is None:
    raise SystemExit("No OpenAI API Key found! Check .env in root") # terminate if there is no API key

# testing client

client = OpenAI()

response = client.chat.completions.create(
    model= 'gpt-6-luna',
    max_completion_tokens= 50,
    messages= [{'role': 'user', 'content':'Say hello.'}],
)

print(response.choices[0].message.content)
print(response.usage)