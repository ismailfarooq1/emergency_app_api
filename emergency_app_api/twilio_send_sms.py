from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC97e6c9c31b3524bb4e8ee5dfbc4a17b6'
auth_token = '7afa61880a41c451ddeedd378bbd6b69'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="\nWe can see you Ibrahim :). Black sweat shirt and blue pants suit you..",
        #  messaging_service_sid='MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
         from_= '+16467603049',
         to='+923350536138'
     )

print(message.sid)


