import os
import requests
from flask import Flask, request

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

app = Flask(__name__)

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)

@app.route("/")
def home():
    return "Bot activo"

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    message = f"""
📈 ALERTA TRADINGVIEW

Par: {data.get('symbol')}
Acción: {data.get('action')}
Precio: {data.get('price')}
Timeframe: {data.get('timeframe')}
"""

    send_telegram(message)

    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)



