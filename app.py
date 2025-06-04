from flask import Flask, request
import requests

app = Flask(__name__)

# اطلاعات شما
BOT_TOKEN = "7551084659:AAGBnxixa_DtS5i_r1e_dXeCGDO29P-JBhA"
CHANNEL_USERNAME = "@yarodqadir"

@app.route("/", methods=["GET"])
def home():
    return "✅ ربات روشنه و فعاله."

@app.route("/payment", methods=["POST"])
def payment():
    data = request.json
    
    payer = data.get("payer", "ناشناس")
    amount = data.get("amount", 0)

    message = f"💳 پرداخت جدید:\n👤 نام: {payer}\n💰 مبلغ: {amount} تومان"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "text": message
    }

    try:
        requests.post(url, json=payload)
    except Exception as e:
        return f"❌ خطا در ارسال پیام: {e}", 500

    return "✅ پیام با موفقیت ارسال شد", 200
