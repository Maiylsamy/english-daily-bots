import requests
import json
BOT_TOKEN = "8501664348:AAE-aR3sQvoQfYJXT8s9bY0sd_xPKU7qIOE"
CHAT_ID = "1342013802"
GEMINI_API_KEY = "AIzaSyAp84j-arnCLtXSIu_JhQZp7EhzT6X4I30"

quote = requests.get("https://zenquotes.io/api/random").json()[0]["q"]

prompt = f"""
You are an English tutor.

1. Explain the sentence in simple English.
2. Translate to Tamil.
3. Create one multiple choice quiz.
4. Provide correct answer.

Sentence:
{quote}

Format:
Simple Meaning:
Tamil:
Quiz:
Answer:
"""

gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

payload = {"contents": [{"parts": [{"text": prompt}]}]}

response = requests.post(gemini_url, json=payload).json()

text = response["candidates"][0]["content"]["parts"][0]["text"]

# Extract answer (simple approach)
answer = text.split("Answer:")[-1].strip()

# Save state
state = {"answer": answer}
with open("quiz_state.json", "w") as f:
    json.dump(state, f)

message = f"📘 Sentence:\n{quote}\n\n{text}"

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(telegram_url, data={"chat_id": CHAT_ID, "text": message})
