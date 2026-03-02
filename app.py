import yfinance as yf
import requests
import time
import os

STOCK_CODE = os.environ.get("STOCK_CODE")
TARGET_PRICE = float(os.environ.get("TARGET_PRICE"))
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

def check_stock():
    stock = yf.Ticker(STOCK_CODE)
    price = stock.history(period="1d")["Close"].iloc[-1]
    print(f"当前价格: {price}")

    if price <= TARGET_PRICE:
        send_telegram_message(f"🔔 {STOCK_CODE} 已跌至 {price}")
        time.sleep(3600)  # 防止刷屏，触发后1小时内不再提醒

while True:
    check_stock()
    time.sleep(60)
