import os
from twilio.rest import CLient

client = Client(account_sid, auth_token)
if (percent_difference > 5): 
  client.messages.create(
   to = os.environ["phone"],
   from = "+18587077533"
   body = "The percent difference in stock since " + %d + " is " + %d + "%" % (time_previous, percent_difference) #first %d is time previous second is percent difference
)
