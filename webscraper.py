from bs4 import BeautifulSoup as BS
import urllib.request as UL
import re

html_page = UL.urlopen("https://www.propertyroom.com/s/rolex")
soup = BS(html_page, "html.parser")
prLink="https://propertyroom.com"

listings=[]

for link in soup.select("a[href*=rolex]"):
    listings.append(link["href"])

listings=list(set(listings))

for link in range(0,len(listings)):

    listingLink=prLink+listings[link]
    print(listingLink)
    listingPage=UL.urlopen(listingLink)
    soup2=BS(listingPage, "html.parser")
    price=soup2.find("li",id="MainContent_uxPrice")
    print (price.text)

# ebthPage= UL.urlopen("https://www.ebth.com/search?q=rolex+watch")
# soupE=BS(ebthPage,"html.parser")
# print (soupE.find_all("a"))