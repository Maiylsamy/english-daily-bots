import requests
import json

BOT_TOKEN = "8501664348:AAE-aR3sQvoQfYJXT8s9bY0sd_xPKU7qIOE"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
updates = requests.get(url).json()

try:
    with open("quiz_state.json") as f:
        state = json.load(f)
        correct = state.get("answer", "").lower()
except:
    correct = ""

for item in updates["result"]:
    if "message" in item:
        chat_id = item["message"]["chat"]["id"]
        text = item["message"].get("text", "").lower().strip()

        if text in ["a", "b", "c", "d"]:
            if text == correct:
                reply = "✅ Correct! Great job."
            else:
                reply = f"❌ Wrong. Correct answer is {correct.upper()}."

            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={"chat_id": chat_id, "text": reply},
            )
