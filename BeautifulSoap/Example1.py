 import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.select('article.product_pod')

top_10 = []
for book in books[:10]:
    title = book.h3.a['title']
    price = book.select_one('p.price_color').text
    top_10.append({'title': title, 'price': price})

for item in top_10:
    print(item['title'], '-', item['price'])
