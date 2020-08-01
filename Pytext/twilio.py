from twilio import Client

account_sid = "Your Account_SID"
auth_token = "Valid Token"

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="....",
    from_="twilio no",
    body="This is our message"
)
