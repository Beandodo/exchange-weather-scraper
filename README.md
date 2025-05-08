# 🌦️ Weather Scraper

這是一個簡單的天氣爬蟲小工具，可以根據使用者輸入的城市名稱，自動查詢該城市的經緯度，並取得即時天氣資訊（使用 Open-Meteo API 和 Nominatim 地理編碼服務）。

## 🔧 安裝方式

1. 建議使用虛擬環境：
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows

安裝套件：


pip install -r requirements.txt
🚀 使用方式
執行主程式：


python weather.py
接著輸入城市名稱（例如：台北、Tokyo、New York），即可顯示天氣資料。

🛠 使用技術
Python

requests

Open-Meteo API

Nominatim API (OpenStreetMap)

📦 其他檔案
weather.py：主程式

requirements.txt：依賴套件清單

.gitignore：忽略的檔案設定


💡 匯率爬蟲小工具程式解說：
API 說明：

使用 ExchangeRate API（免費無需 API 金鑰）

API 格式：

arduino
複製
編輯
https://api.exchangerate.host/latest?base=USD&symbols=TWD
base：基準貨幣

symbols：目標貨幣

程式流程：

使用者輸入 基準貨幣 和 目標貨幣

程式呼叫 API 並取得匯率

顯示匯率資訊


