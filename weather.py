#https://open-meteo.com/
# exchange-weather-scraper/
# ├── .venv/
# ├── weather.py
# ├── exchange.py
# ├── main.py
# ├── README.md
# ├── requirements.txt
# └── .gitignore
import requests

def get_coordinates(city):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json"
    }
    try:
        response = requests.get(url, params=params, headers={"User-Agent": "weather-app"})
        response.raise_for_status()
        data = response.json()
        if data:
            latitude = float(data[0]["lat"])
            longitude = float(data[0]["lon"])
            return latitude, longitude
        else:
            print("❌ 找不到該城市的位置")
            return None, None
    except requests.RequestException as e:
        print("❌ 取得經緯度失敗：", e)
        return None, None

def get_weather(latitude, longitude, city_name):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&current_weather=true"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        current = data["current_weather"]

        print(f"\n📍 天氣資訊（{city_name}）")
        print(f"🌡️ 溫度：{current['temperature']}°C")
        print(f"💨 風速：{current['windspeed']} km/h")
        print(f"⏰ 時間：{current['time']}")

    except requests.RequestException as e:
        print("❌ 無法取得天氣資料:", e)

if __name__ == "__main__":
    city = input("請輸入要查詢天氣的城市名稱：")
    lat, lon = get_coordinates(city)
    if lat and lon:
        get_weather(lat, lon, city)
