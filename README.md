# python-twilio
# Free SMS Using Twilio and Python

### 1. Setup Twilio Account
#####  Go to the Twilio site and get register yourself. https://www.twilio.com/
![Twillio Register](https://i.ibb.co/hF7JvBX/screenshot-www-twilio-com-2023-01-19-10-28-02.png)

### 2. Once you get registered, verify your Email ID.
### 3. Once your email id gets verified, you need to add and verify your mobile number. (You will receive the OTP)
![Twillio OTP](https://i.ibb.co/wg1rmL5/twill-otp.png)

### 4. After mobile and email verification fill in the basic information.
![Twillio Bisc info](https://i.ibb.co/YQ61MVJ/1-te-XA-g-C1-VF7-ZUF-a-B1h5lg.png)

### 5. Twilio provides a virtual mobile number to send the SMS for the free account. You need to click on the (Get Virtual Phone Number) button.
![Twillio Virtual number](https://i.ibb.co/Jqgs2QH/1-a-Jm7agvyi-V0-Aor-INOq3-Eu-A.png)

### 6. Grab the Account SID, Account Token, and Twilio Virtual Phone Number.
```
Account SID is a security identifier.
Account Token used to access the API
```
![Twillio keys](https://i.ibb.co/W66bfZ8/1-L7-Vw-PSOxkb-Eshz-Tg4-A5nb-Q.png)

### 7. For the trail/free version, you can only send messages to verified caller ids.

## Integrating Twilio API using Python

### 1. Create/Setup a Python virtual environment
```
# install the virtual environment
>>> pip3 install -U virtualenv
>>> mkdir python-twilio-sender
>>> cd python-twilio-sender
>>> virtualenv venv
# activate the virtual environment
>>> source venv/bin/activate
(venv) prompt$
```
### 2. Install twilio python library/SDK
https://www.twilio.com/docs/libraries/python#install-the-library
```
>>> pip3 install twilio
```

### 3. Simple code snippet to send the SMS
```
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "<account_sid>"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)
message = client.messages.create(
    to="+15558675309", 
    from_="+15017250604",
    body="Hello from Python!")
print(message.sid)
```

### 4. Complete API document https://www.twilio.com/docs/sms/quickstart/python

#### Notes :
#####  A) Auth token and Account SID must be sorted in the OS.
##### Reference: https://docs.python.org/3/library/os.html#os.environ
##### B) For the trial version “to” number must be first verified.
