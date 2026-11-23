import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # load environment variables

client = OpenAI() # define the client

# Define the model to use
model = "gpt-6-luna"

# sets the role, scope and rules for the chatbot for the entire conversation
system_msg = '''
                You are a helpful Malaysian travel expert who can deliver valuable insights into Kuala Lumpur's iconic landmarks and hidden gems. 
                You work for a well-known tour company in Malaysia and aim to deliver an immersive travel planning experience for its clientele. Always give distances in kilometres. 
                Only answer questions about travelling in Kuala Lumpur, including attractions, itineraries, food, weather, transport, and safety tips. 
                If a question is about anything else, including other parts of Malaysia, reply exactly with: "Sorry, I can only help with trip-related questions about Kuala Lumpur.
                Reply in plain text without Markdown.
             '''

# conversation history, system message and few-shot examples showing the desired answer style
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
        {
        'role': 'user',
        'content': 'Where is Stadium Negara?'
    },
    {
        'role': 'assistant',
        'content': 'Stadium Negara is in central Kuala Lumpur, right next to Stadium Merdeka and the Merdeka 118 tower. It is a short walk from Petaling Street in Chinatown, making it easy to combine with a heritage walk around the old city. Enjoy exploring!'
    },
    {
        'role': 'user',
        'content': 'What are the must-visit attractions in Bukit Bintang?'
    },
    {
        'role': 'assistant',
        'content': 'Here are a few must-visit spots in Bukit Bintang:\n- Jalan Alor: a lively street-food strip, best in the evening.\n- Pavilion Kuala Lumpur: a major shopping centre with plenty of dining options.\n- Lot 10 Hutong: a food court featuring well-known local hawker favourites.\n- Changkat Bukit Bintang: a buzzing street of bars and restaurants.\nEnjoy your time in the heart of KL!'
    },

]

while True: # keep chatting until user quits
    question = input('Please Ask a Question to the Chatbot about Kuala Lumpur related queries. (Type "QUIT" to exit): ')

    if question.strip().lower() == 'quit': # exit before making an API call
        break

    if not question.strip(): # skip empty input without calling the API
        continue

    user_message = {'role': 'user','content': question}  # add the user's question to the history
    conversation.append(user_message)

    response = client.chat.completions.create(
        model=model,
        max_completion_tokens=700,
        reasoning_effort="low", # replaces temperature for reasoning models
        messages=conversation
    )

    assistant_response = {'role': 'assistant','content': response.choices[0].message.content} # extract the reply text
    conversation.append(assistant_response) # save the reply for follow up questions
    print("Assistant: ", response.choices[0].message.content, "\n")
    
    
