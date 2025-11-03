# start_bot.py - minimal, safe, uses BOT_TOKEN from Render env
import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

BOT_TOKEN = os.environ.get("8511737410:AAEOveq7ceKVRtKehrXIH_-uGp-GVGW4BHA")  
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

@app.route("/", methods=["GET"])
def index():
    return "Bot running", 200

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    # defensive parsing
    message = (data or {}).get("message", {})
    text = message.get("text", "")
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    if text == "/start" and chat_id:
        send_message(chat_id, "👋 Hello! Bot is online and ready.")
    return jsonify({"ok": True}), 200

def send_message(chat_id, text):
    try:
        requests.post(API_URL + "sendMessage", json={"chat_id": chat_id, "text": text}, timeout=10)
    except Exception:
        pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

def index():
    return "Bot is running!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
