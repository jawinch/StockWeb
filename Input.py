accountSID = raw_input("Account SID: ")
authToken = raw_input("Authorization Token: ")
phoneNumber = raw_input("Phone Number: ")

import urllib.request 
#basil

def main():
  webUrl = urllib.request.urlopen("https://www.nasdaq.com/market-activity/stocks/tsla")
  
  print ("result code: " + str(webUrl.getcode()))
  
  # read the data from the URL and print it
  data = webUrl.read()
  print (data)

if __name__ == "__main__":
  main() 
#basil
