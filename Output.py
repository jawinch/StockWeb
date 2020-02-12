import os
from twilio.rest import Client

auth_token =  "9ac2fcd49949b7464ebb7990e2f80226" #os.environ["twillio_token"]
account_sid = "AC490240393f307819b0706cb4040cd82f" #os.environ["twillio_account"]
percent_difference = 5
time_previous = "15:30"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to = "+15039533843", #os.environ["phone"],
    from_= "+18587077533",
    body = "The percent difference in stock since " + %s + " is " + %d + "%" % (time_previous, percent_difference) #first %s is time previous second is percent difference
)
if (percent_difference >= 5):
    print(message.sid)

    #"The percent difference in stock since " + %s + " is " + %d + "%" % (time_previous, percent_difference) #first %s is time previous second is percent difference
