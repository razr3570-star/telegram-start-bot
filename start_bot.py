import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = 8511737410:AAEOveq7ceKVRtKehrXIH_-uGp-GVGW4BHA
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id, text):
    """Send message to user."""
    url = f"{BASE_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "👋 Hello Master! I’m online and ready to serve. What would you like to know today?")
        else:
            send_message(chat_id, "Please use /start to begin.")

    return {"ok": True}

@app.route("/", methods=["GET"])
def home():
    return "Bot is running fine!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
