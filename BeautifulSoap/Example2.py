import requests
from bs4 import BeautifulSoup

url = "https://www.lush.com/us/en_us/p/moomintroll-bath-bomb"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

session = requests.Session()       
response = session.get(url,headers=headers)        

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1", class_="text-product-name-pdp font-handwritten mb-2 break-words text-inherit grid-area-[name]")
print(title.text.strip() if title else "Title not found")

price = soup.find('span', class_='text-subtitle-three')
print(price.text.strip() if price else "Price not found")
