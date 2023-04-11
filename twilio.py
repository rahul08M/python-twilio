from twilio.rest import Client    # Import Client class from twilio module

# Your Account SID from twilio.com/console
account_sid = "AC99ca7a2839539a376682fb74cbb239e0"    # account sid

# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"    # auth token

client = Client(account_sid, auth_token)    # initialize client object

message = client.messages.create(
    to="+15558675309",    # receiver mobile number
    from_="+15017250604",    # sender mobile number
    body="Hello from Python!"    # message
)
