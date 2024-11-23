from bs4 import BeautifulSoup
import requests

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, features="html.parser")

books = [
    soup.find_all("h3"),
    soup.find_all("p", {"class": "price_color"})
]

file= open("books.txt", 'w')
for i in range(0, len(books[0])):
    print(f"{books[0][i].text} {books[1][i].text}")

file.close()
time.sleep(5)