import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Website
url = "https://books.toscrape.com/"

 
driver = webdriver.Chrome()
driver.get(url)

# Store all books
all_books = []

while True:

 
    time.sleep(2)

    
    soup = BeautifulSoup(driver.page_source, "html.parser")

 
    books = soup.select("article.product_pod")

 
    for book in books:

        title = book.select_one("h3 a")
        price = book.select_one(".price_color")
        availability = book.select_one(".availability")

        all_books.append({
            "Title": title.get("title") if title else "N/A",
            "Price": price.get_text(strip=True) if price else "N/A",
            "Availability": availability.get_text(strip=True)
            if availability else "N/A"
        })

    print(f"Page scraped. Books collected: {len(all_books)}")

 
    next_button = driver.find_elements(
        By.CSS_SELECTOR,
        "li.next a"
    )

 
    if not next_button:
        print("No more pages.")
        break

  
    next_button[0].click()

   
    time.sleep(2)

 
driver.quit()

 df = pd.DataFrame(all_books)

df.to_excel(
    "books.xlsx",
    index=False
)

print("Done!")
print(f"Total books scraped: {len(df)}")
