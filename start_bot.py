import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ.get 8511737410:AAEOveq7ceKVRtKehrXIH_-uGp-GVGW4BHA # token stored safely in Render
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def respond():
    update = request.get_json()
    message = update.get("message", {}).get("text", "")
    chat_id = update.get("message", {}).get("chat", {}).get("id")

    if message == "/start":
        send_message(chat_id, "👋 Hello! I’m your bot. I’ll soon give you Forex updates and news!")
    else:
        send_message(chat_id, "Please type /start to begin.")

    return "ok", 200

def send_message(chat_id, text):
    url = API_URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

@app.route("/")
def index():
    return "Bot is running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
