from bs4 import BeautifulSoup #E
import Requests #E

link = requests.get('https://www.nasdaq.com/market-activity/stocks/tsla') #E

#class of current stock price: "symbol-page-header__pricing-price"
# @Ethan, rewrite using beautiful soup stuff, this might also be complete bs and I don't know what I'm talking about
def handle_starttag(tag,class,attrs):
  if tag == "span" and class == "symbol-page-header__pricing-price":
    currentValue = class.contents

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
    
  # open the sample HTML file and read it
  f = open("samplehtml.html")
  if f.mode == "r":
    contents = f.read() # read the entire file
    parser.feed(contents)

if __name__ == "__main__":
  main();
#basil
