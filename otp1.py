from twilio.rest import Client

account_sid = 'AC629eed84beccd0e3ca7bcda547c9530e'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12028131526',
  body='Have a Good Day!!',
  to='+919356152157'
)

print(message.sid)