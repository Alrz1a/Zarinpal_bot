from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7551084659:AAGBnxixa_DtS5i_r1e_dXeCGDO29P-JBhA'
CHANNEL_ID = '@yarodqadir'

@app.route('/zarinpal', methods=['POST'])
def zarinpal_webhook():
    data = request.json
    if data and data.get("status") == "OK":
        user = data.get("user", "Unknown user")
        amount = data.get("amount", "Unknown amount")
        msg = f"✅ پرداخت جدید:\n👤 کاربر: {user}\n💳 مبلغ: {amount} تومان"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHANNEL_ID,
            "text": msg
        }
        requests.post(url, json=payload)
    return "OK"

@app.route('/')
def home():
    return 'ربات فعال است ✅'
