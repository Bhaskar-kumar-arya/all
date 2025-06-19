from bs4 import BeautifulSoup
import requests
import re

def extractBooks () : 
    url = "http://books.toscrape.com/"
    result = requests.get(url)
    doc = BeautifulSoup(result.text,"html.parser")
    books = doc.find_all("article",class_ = "product_pod") 
    for book in books :
        title = book.find("h3").a["title"]
        price = book.find("p",class_ = "price_color").text
        imageURL = book.find("img")["src"]
        print(title,price,imageURL)
   # print(doc.find_all(string = re.compile("stock",re.IGNORECASE)))

extractBooks()