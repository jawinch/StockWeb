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
olderValue = soup.find("span", class_="symbol-page-header__pricing-price").text


# to get second data set
browser.get("https://www.nasdaq.com/market-activity/stocks/tsla")

# Beautiful soup scrape stock ticker price
sleep(15)
soup = BeautifulSoup(browser.page_source, "html.parser")
currentValue = soup.find("span", class_="symbol-page-header__pricing-price").text #Change current value
#while currentvalue is within range, wait X seconds then run code again to get the new value,
#if its out of range, what do we print?
while (olderValue-5 <= currentValue <= olderValue+5) == True:
    sleep(15)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    currentValue = soup.find("span", class_="symbol-page-header__pricing-price").text #Change current value
    else:
        return(currentValue)#did we want something else?
        break

print(currentValue) #E
