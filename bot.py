import requests

BOT_TOKEN = "8501664348:AAE-aR3sQvoQfYJXT8s9bY0sd_xPKU7qIOE"
CHAT_ID = "1342013802"

quote = requests.get("https://zenquotes.io/api/random").json()[0]["q"]

message = f"Daily English:\n\n{quote}"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={"chat_id": CHAT_ID, "text": message})
