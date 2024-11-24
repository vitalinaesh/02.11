from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.quotegarden.com/mind.html')
soup = BeautifulSoup(response.text, features="html.parser")

texts = soup.find_all(["p","div", "blockquote"])

for i in range(len(texts)):
    print(f'{texts[i]}')


