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
  	body = "I thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic, he could save others from death, but not himself.

")
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
