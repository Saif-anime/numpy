from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create a Twilio client
client = Client(account_sid, auth_token)

# List of phone numbers to send messages to
phone_numbers = ['8196902529']  # Add the phone numbers you want to send messages to

# Message to send
message_body = 'Hello, this is a bulk SMS message from Python!'

# Send messages to each phone number
for phone_number in phone_numbers:
    message = client.messages.create(
        body=message_body,
        from_='8196902529',  # Your Twilio phone number
        to=phone_number
    )
    print(f"Message sent to {phone_number}: {message.sid}")
