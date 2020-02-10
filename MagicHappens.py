from bs4 import BeautifulSoup #E
import Requests #E

link = requests.get('https://www.nasdaq.com/market-activity/stocks/tsla') #E

#class of current stock price: "symbol-page-header__pricing-price"
def handle_starttag(tag,class,attrs):
  if tag == "meta" and class == "symbol-page-header__pricing-price":
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
