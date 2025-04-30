import requests

response = requests.get("https://wttr.in/Taipei?format=3")
print(response.text)

# import requests

# city = "Taipei"
# url = f"https://wttr.in/{city}?format=3"  # 簡潔格式：地點 + 天氣 + 氣溫

# response = requests.get(url)
# print(response.text)
