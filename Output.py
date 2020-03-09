from twilio.rest import Client
from input.py import client
from input.py import accountSID
from input.py import authToken
from input.py import phoneNumber
from input.py import twilioPhone
from MagicHappens.py import timePrevious
from MagicHappens.py import percentDifference

percentDifference = 5
timePrevious = "15:30"

client = Client(accountSid, authToken)

message = client.messages.create(
    to = phoneNumber,
    from_= twilioPhone,
    body = "The percent difference in stock since " + %s + " is " + %d + "%" % (time_previous, percent_difference) #first %s is time previous second is percent difference
)
if (percentDifference >= 5):
    print(message.sid)
  

    #"The percent difference in stock since " + %s + " is " + %d + "%" % (time_previous, percent_difference) #first %s is time previous second is percent difference
