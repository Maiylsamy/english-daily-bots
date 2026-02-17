import requests

BOT_TOKEN = "8501664348:AAE-aR3sQvoQfYJXT8s9bY0sd_xPKU7qIOE"
CHAT_ID = "1342013802"
GEMINI_API_KEY = "AIzaSyDIckYdktw-LoNBTjsTwQdMqVc30HNVamQ"

quote = requests.get("https://zenquotes.io/api/random").json()[0]["q"]

prompt = f"Explain this sentence in very simple English for a beginner:\n\n{quote}"

gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

payload = {
    "contents": [
        {
            "parts": [{"text": prompt}]
        }
    ]
}

response = requests.post(gemini_url, json=payload).json()

meaning = response["candidates"][0]["content"]["parts"][0]["text"]

message = f"📘 Sentence:\n{quote}\n\n🧠 Simple Meaning:\n{meaning}"

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(telegram_url, data={"chat_id": CHAT_ID, "text": message})
