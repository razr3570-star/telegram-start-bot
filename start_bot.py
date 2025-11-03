from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("8511737410:AAEOveq7ceKVRtKehrXIH_-uGp-GVGW4BHA")
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            requests.post(TELEGRAM_URL, json={"chat_id": chat_id, "text": "Hey there! 👋 Your bot is live!"})
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
