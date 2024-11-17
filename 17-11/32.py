from bs4 import BeautifulSoup
import requests
# response = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
# print(response.content)
# soup = BeautifulSoup(response.text, features="html.parser")
# bictoin = soup.find("span", {"class": "sc-65e7f566-0 WXGwg base-text"})
# print(bictoin.text)

response = requests.get("https://coinmarketcap.com/currencies/")
soup = BeautifulSoup(response.text, features="html.parser")
coins = soup.find_all()

