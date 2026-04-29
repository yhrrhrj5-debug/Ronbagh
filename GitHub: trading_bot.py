import requests
import time
from datetime import datetime

def get_btc_price():
    # كيجيب الثمن من بينانس
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    try:
        response = requests.get(url)
        data = response.json()
        return float(data['price'])
    except:
        return None

def start_bot():
    # حدد الثمن اللي باغي تشري فيه (مثلا 64000)
    target_buy = 60000.0 
    # حدد الثمن اللي باغي تبيع فيه (مثلا 70000)
    target_sell = 75000.0 

    print("--- البوت خدام دابا ---")
    print(f"هدف الشراء: {target_buy} | هدف البيع: {target_sell}")
    print("-----------------------")

    while True:
        price = get_btc_price()
        now = datetime.now().strftime("%H:%M:%S")

        if price:
            print(f"[{now}] الثمن الحالي: {price}$")
            
            if price <= target_buy:
                print(">>> فرصـة شـراء! الثمن هبط للهدف ديالك.")
            
            elif price >= target_sell:
                print(">>> فرصـة بيـع! الثمن وصل للربح اللي بغيتي.")
        else:
            print(f"[{now}] مشكل فالاتصال.. غنعاود نحاول.")

        # كيتسنى دقيقة (60 ثانية) باش ما يسهلكش البري والأنترنيت
        time.sleep(60)

if __name__ == "__main__":
    start_bot()
