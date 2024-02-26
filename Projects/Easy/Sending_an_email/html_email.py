# Sending an email using gmail
#Enable the allow app access to on in the gmail security settings

import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from python"
body = "This is a test email from python program"
sender_email = "test@test.com" #replace the gmail address when sending the email 
reciever_email = "abc@test.com"
password = input("Enter the password")


message = EmailMessage()
message["From"] = sender_email
message["To"] = reciever_email
message[subject] = subject

#Sending the html in the email using the triple-quoted f-string 
html = f"""
<html>
<body>
<h1> Hello </h1>
<p> Hi </p>
</body>
</html>

"""

# Adding the html to the message and setting the subtype top html
message.add_alternative(html, subtype="html")

# When we connect the gmail server, we are using the SSL to connect using the SMPT library securely
context = ssl.create_default_context
print("Sending Email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message.as_string)

print("Email Sent successfully")