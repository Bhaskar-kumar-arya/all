from bs4 import BeautifulSoup

with open("beautifulSoup\\index.html","r") as file :
    doc = BeautifulSoup(file,"html.parser")
    doc.i.string = "i changed it "
    print(doc.i.string)    