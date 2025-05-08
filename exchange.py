import requests
from bs4 import BeautifulSoup

def get_usd_rate():
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    usd_row = soup.find("td", text="USD 美金").find_parent("tr")
    rate = usd_row.find_all("td")[2].text.strip()  # 現金買入
    return f"USD 現金買入匯率：{rate}"
