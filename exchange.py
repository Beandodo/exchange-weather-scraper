import requests

def get_exchange_rate(base_currency="USD", target_currency="TWD"):
    url = (
        f"https://api.exchangerate.host/latest?"
        f"base={base_currency}&symbols={target_currency}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"][target_currency]

        print(f"💱 匯率資訊：1 {base_currency} = {rate} {target_currency}")

    except requests.RequestException as e:
        print("❌ 無法取得匯率資料:", e)

if __name__ == "__main__":
    base = input("請輸入基準貨幣（如 USD）：").upper()
    target = input("請輸入目標貨幣（如 TWD）：").upper()
    get_exchange_rate(base, target)
