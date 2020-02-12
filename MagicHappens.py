from bs4 import BeautifulSoup #E
import Requests #E

#class of current stock price: "symbol-page-header__pricing-price"
# @Ethan, rewrite using beautiful soup stuff, this might also be complete bs and I don't know what I'm talking about
def handle_starttag(tag,class,attrs): #B
  if tag == "span" and class == "symbol-page-header__pricing-price": #B
    global previousValue = currentValue #B
    global currentValue = class.contents #B

def main(): #B
  link = requests.get('https://www.nasdaq.com/market-activity/stocks/tsla') #E
  parser = MyHTMLParser() #B
    
  f = open("samplehtml.html") #B
  if f.mode == "r": #B
    contents = f.read() #B
    parser.feed(contents) #B

if __name__ == "__main__":
  main();
#basil
