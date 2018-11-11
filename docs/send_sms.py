# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send_sms(msg):
	# Your Account Sid and Auth Token from twilio.com/console
	account_sid = 'AC2acbffc73404d20afff48696c6d435be'
	auth_token = '9da5af117fd3a0c7633d2b84b02463aa'
	client = Client(account_sid, auth_token)

	message = client.messages \
	                .create(
	                     body=msg,
	                     from_='+16078214455',
	                     to='+12035354858'
	                 )

	print(message.sid)