from twilio.rest import Client
from bs4 import BeautifulSoup #E
import requests #E
from time import sleep #E
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import time #j
from datetime import date #j
from datetime import timedelta #j

global phone
global tPhone
global accountSID
global authToken
global phoneNumber
global twilioPhone
global link
global client
global message
global messageReceived
global options
global firefox_capabilities
global browser
global soup
global currentValue
global percentDifference
global timePrevious


def input():
  
	accountSID = input("Account SID: ") #b

	authToken = input("Authorization Token: ") #b

	phoneNumber = input("Phone Number: ") #b
	twilioPhone = input("Twilio Number: ")
	while (len(phoneNumber) != 10 or not phoneNumber.isdigit()):
  		print("Phone number should be 10 numbers")
  		phoneNumber = input("Phone Number: ") #b
	while (len(twilioPhone) != 10 or not twilioPhone.isdigit()):
  		print("Twilio number should be 10 numbers")
  		twilioPhone = input("Twilio Number: ") #b
	if ((len(twilioPhone) == 10) and twilioPhone.isdigit()): #j
		tPhone = 1 #j
	else: #j
		tPhone = 0 #j	
	if ((len(phoneNumber) == 10) and phoneNumber.isdigit()): #j
		Phone = 1 #j
	else:
		Phone = 0 #j
	link = input("NASDAQ Website Link: ") #E 

	client = Client(accountSID,authToken) #j
	message = client.messages.create( #j
  		to = phoneNumber, #j
  		from_ = twilioPhone, #j
  		body = "Did you ever hear the tragedy of Darth Plagueis?(Look at command prompt)") #j
	print(message.sid)# j

	messageReceived = input("Fear leads to anger. Anger leads to hate. Did you receive this message?('yes' or 'no')") #b

	def ask(): #b
  		if (messageReceived == "yes"): #b
  			print("Thanks for using the sytem.") #b
  		elif (messageReceived == "no"): #b
  			main() #b
  		else: #b
  			ask() #b
	magic()



def magic():

	# The NASDAQ webpage uses javascript to load the stock price. Without javascript enabled,
	# there's no stock ticker price. In order to get around this, we use Selenium to run Firefox
	# to load the javascript, and get the stock ticker price.

	# To do this, we need Firefox installed, and we need to download geckodriver from
	# https://github.com/mozilla/geckodriver/releases and put the binary in this directory.

	# Import selenium libraries


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

	# Beautiful soup scrape stock ticker price
# 	sleep(15)
# 	soup = BeautifulSoup(browser.page_source, "html.parser")
# 	currentValue = soup.find("span", class_="symbol-page-header__pricing-price").text #Change current value
# 	#while currentvalue is within range, wait X seconds then run code again to get the new value,
# 	#if its out of range, what do we print?
# 	while (olderValue-5 <= currentValue <= olderValue+5) == True:
#  	  sleep(15)
#  	  soup = BeautifulSoup(browser.page_source, "html.parser")
#   	  currentValue = soup.find("span", class_="symbol-page-header__pricing-price").text #Change current value
# 	else:
#    	 return(currentValue)#did we want something else?
#    	 break


	# print(currentValue) #E
	output()


def output():
	import requests #E
	from time import sleep #E
	from datetime import time #j
	from datetime import date #j
	import timedelta #j
	percentDifference = 5
	timePrevious = "15:30"

	message = client.messages.create(
    	to = phoneNumber,
    	from_= twilioPhone,
    	#body = "The percent difference in stock since " + %s + " is " + %d + "%" % (time_previous, percent_difference)
    	body = "tepitytest" #first %s is time previous second is percent difference
	)
	if (percentDifference >= 5):
		print(message.sid)
	time.sleep(120)
	magic()

    #"The percent difference in stock since " + %s + " is " + %d + "%" % (time_previous, percent_difference) #first %s is time previous second is percent difference

#if __name__ == "__main__":
input()
