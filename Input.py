from twilio.rest import Client

def main():
  
	accountSID = input("Account SID: ") #b

	authToken = input("Authorization Token: ") #b

	phoneNumber = input("Phone Number: ") #b
	while (len(phoneNumber) != 10 or not phoneNumber.isdigit()):
  		print("Phone number should be 10 numbers")
  		phoneNumber = input("Phone Number: ") #b

  	twilioPhone = input("Twilio Number: ")
  	while (len(twilioPhone) != 10 or not twilioPhone.isdigit()):
  		print("Twilio number should be 10 numbers")
  		twilioPhone = input("Twilio Number: ") #b

  	link = input("NASDAQ Website Link: ") #E 

	client = Client(accountSID, authToken) #j
	message = client.messages.create( #j
  		to = phoneNumber, #j
  		from_ = twilioPhone, #j
  		body = "Is this the correct phone number?") #j
	print(message.sid)# j

	messageReceived = input("Fear leads to anger. Anger leads to hate. Did you receive this message?('yes' or 'no')") #b
	
	def ask(): #b
  		if (messageReceived == "yes"): #b
  			print("Thanks for using the sytem.") #b
  		elif (messageReceived == "no"): #b
  			main() #b
  		else: #b
  			ask() #b

if __name__ == "__main__":
	main();
