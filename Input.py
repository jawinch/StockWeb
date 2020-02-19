import twillio.rest import Client

def main():
  
  accountSID = input("Account SID: ") #b
  authToken = input("Authorization Token: ") #b
  phoneNumber = input("Phone Number: ") #b
  while (len(phoneNumber) != 10 or not phoneNumber.isdigit()):
  	print("Phone number should be 10 numbers")
  	phoneNumber = input("Phone Number: ") #b
  while (len(phoneNumber) != 10 or not phoneNumber.isdigit()):
  	print("Phone number should be 10 numbers")
  	phoneNumber = input("Phone Number: ") #b
  link = input("NASDAQ Website Link: ") #E 

  client = Client(accountSID, authToken)
  message = client.message.create(
  	to = phoneNumber,
  	from_ = "+18587077533",
  	body = "Is this the correct phone number?")
  print(message.sid)

  messageReceived = input("Did you receive the message?('yes' or 'no')")
  def ask():
  	if (messageReceived == "yes"):
  	elif (messageReceived == "no"):
  		main()
  	else:
  		ask()

if __name__ == "__main__":
  main();
