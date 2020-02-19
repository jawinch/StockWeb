from twilio.rest import Client
from input.py import client
from input.py import accountSID
from input.py import authToken
from input.py import to
from input.py import from_
#from output.py import timePrevious
#from output.py import percentDifference

percentDifference = 5
timePrevious = "15:30"

client = Client(accountSid, authToken)

message = client.messages.create(
    to = "+15039533843", #os.environ["phone"],
    from_= "+18587077533",
    body = "The percent difference in stock since " + %s + " is " + %d + "%" % (time_previous, percent_difference) #first %s is time previous second is percent difference
)
if (percentDifference >= 5):
    print(message.sid)
  

    #"The percent difference in stock since " + %s + " is " + %d + "%" % (time_previous, percent_difference) #first %s is time previous second is percent difference
