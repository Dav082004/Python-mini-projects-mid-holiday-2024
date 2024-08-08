import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Retrieve email credentials from environment variables
your_email = os.getenv('EMAIL_ADDRESS')
#The password is found with two-step verification
your_password = os.getenv('EMAIL_PASSWORD')

recipent = 'prueba@gmail.com'

# Create a MIME multipart message object
message = MIMEMultipart()
message['From'] = your_email
message['To'] = recipent
message['Subject'] = 'Colocar titulo'

# Create the body of the email
body = 'Introducir cuerpo que se enviara'
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send the email
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(your_email, your_password)

smtp_server.sendmail(your_email, recipent, message.as_string())
smtp_server.quit()

print('Email enviado')
