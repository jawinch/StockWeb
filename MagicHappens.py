# from bs4 import BeautifulSoup #E
# import Requests #E

# #class of current stock price: "symbol-page-header__pricing-price"
# # @Ethan, rewrite using beautiful soup stuff, this might also be complete bs and I don't know what I'm talking about
# def handle_starttag(tag,class,attrs): #B
#   if tag == "span" and class == "symbol-page-header__pricing-price": #B
#     global previousValue = currentValue #B
#     global currentValue = class.contents #B

# def main(): #B
#   link = requests.get('https://www.nasdaq.com/market-activity/stocks/tsla') #E
#   #link = requests.get(global link) #E
#   parser = MyHTMLParser() #B
    
#   f = open("samplehtml.html") #B
#   if f.mode == "r": #B
#     contents = f.read() #B
#     parser.feed(contents) #B

# if __name__ == "__main__":
#   main();
# #basil

from bs4 import BeautifulSoup #E
import requests #E
from time import sleep #E

##data = '<span class="symbol-page-header__pricing-price">$899.41</span>'
##soup = BeautifulSoup(data)
##t = soup.find('span',{'class': 'symbol-page-header__pricing-price'})
##print (t.text)
page = requests.get('https://www.nasdaq.com/market-activity/stocks/tsla') #E
soup = BeautifulSoup(page.content, 'html.parser') #E
currentValue = soup.find("span", class_="symbol-page-header__pricing-price") #E

##sleep(1) #Waits the program for X seconds #E
##newprice = soup.find("span", class_="symbol-page-header__pricing-price") #newprice E

##while True (price-5) < newprice < (price+5):
##  sleep(5)
##  newprice = soup.find("span", class_="symbol-page-header__pricing-price") #newprice E
##else:
##  break
##return newprice
##return price

print(currentValue) #E
