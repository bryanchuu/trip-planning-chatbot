import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # load environment variables

client = OpenAI() # define the client

# Define the model to use
model = "gpt-6-luna"


system_msg = "You are a helpful Malaysian travel expert who can deliver valuable insights into Kuala Lumpur's iconic landmarks and hidden gems. You work for a well-known tour company in Malaysia and aim to deliver an immersive travel planning experience for its clientele. Always give distances in kilometres."

conversation = [
    {
        'role': 'system',
        'content': system_msg
    },
    {
        'role': 'user',
        'content': 'Hello, how far away is Merdeka Square from the Petronas Twin Towers if you are driving, in km?'
    },
    {
        'role': 'assistant',
        'content': 'Merdeka Square is about 3 to 4 km from the Petronas Twin Towers by car. Depending on traffic, the drive typically takes around 10 to 25 minutes. Enjoy your visit to these iconic landmarks!'
    },

]
question_list = [
    "How far away is Batu Caves from the Petronas Twin Towers in kilometres if you are driving?",
    "Where is Stadium Negara?",
    "What are the must-visit attractions in Bukit Bintang?"
                    ]

for question in question_list:
    print("User: ", question)
    user_message = {'role': 'user','content': question}
    conversation.append(user_message)

    response = client.chat.completions.create(
        model=model,
        max_completion_tokens=200,
        reasoning_effort="low", # replaces temperature for reasoning models
        messages=conversation
    )

    assistant_response = {'role': 'assistant','content': response.choices[0].message.content}
    conversation.append(assistant_response)
    print("Assistant: ", response.choices[0].message.content, "\n")
    
