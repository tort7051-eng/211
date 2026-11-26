import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

while url:
    response = requests.get(url, timeout=30)
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.find_all("article", class_="product_pod"):
        print(book.h3.a["title"])

    next_page = soup.find("li", class_="next")

    if next_page:
        url = urljoin(url, next_page.a["href"])
    else:
        url = None