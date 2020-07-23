import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005380"
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

no_today = bs_obj.find("p", {"class": "no_today"})
blind = no_today.find("span", {"class": "blind"})
now_price = blind.text
 
print(now_price)