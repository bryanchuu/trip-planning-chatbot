# Kuala Lumpur Trip-Planning Chatbot

An interactive command-line travel assistant for Kuala Lumpur, built with the OpenAI API.

## About

This project is adapted from DataCamp's **Paris trip-planning chatbot** project (Associate AI Engineer for Developers track). The original sent a fixed list of predetermined questions to the model. This version lets you **chat with the bot live**: ask your own questions, ask follow-ups, and quit when you're done.

### Changes from the original

- **Interactive chat:** type your own questions in the terminal instead of using a static question list
- **Conversation memory:** the full chat history is sent with each request, so follow-up questions work
- **Localized to Kuala Lumpur:** new system prompt and few-shot examples, with distances in kilometres
- **Topic restriction:** only answers trip-related questions about Kuala Lumpur and politely declines anything else
- **Reasoning model:** uses `max_completion_tokens` and `reasoning_effort` instead of `temperature`

## Setup

1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-key-here
   ```

## Usage

```bash
python trip_planning_chatbot.py
```

Ask questions about Kuala Lumpur, such as itineraries, attractions, food, transport or distances. Type `quit` to exit.

## Files

- `trip_planning_chatbot.py`: the chatbot
- `test_api.py`: quick check that your API key and environment work
- `requirements.txt`: pinned dependencies