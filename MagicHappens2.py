from bs4 import BeautifulSoup #E
import requests #E
from time import sleep #E



# The NASDAQ webpage uses javascript to load the stock price. Without javascript enabled,
# there's no stock ticker price. In order to get around this, we use Selenium to run Firefox
# to load the javascript, and get the stock ticker price.

# To do this, we need Firefox installed, and we need to download geckodriver from
# https://github.com/mozilla/geckodriver/releases and put the binary in this directory.

# Import selenium libraries
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Run firefox without opening a window (headless mode)
options = Options()
options.headless = True

# Tell selenium where firefox and geckodriver are
firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
browser = webdriver.Firefox(options=options, executable_path=r'geckodriver.exe', capabilities=firefox_capabilities)

# Load and run javascript on webiste
browser.get("https://www.nasdaq.com/market-activity/stocks/tsla")

# Beautiful soup scrape stock ticker price
soup = BeautifulSoup(browser.page_source, "html.parser")
currentValue = soup.find("span", class_="symbol-page-header__pricing-price").text


# to get second data set
browser.get("https://www.nasdaq.com/market-activity/stocks/tsla")

# Beautiful soup scrape stock ticker price
soup = BeautifulSoup(browser.page_source, "html.parser")
currentValue = soup.find("span", class_="symbol-page-header__pricing-price").text #Change current value

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
