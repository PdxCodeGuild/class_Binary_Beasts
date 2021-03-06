import api # Import my api lab
import smtplib, ssl # import to send emails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from secrets import cod_kill_gmail # import email password

port = 465 # For SSL
smtp_server = "smtp.gmail.com" # gmail server
sender_email = "code.killer1968@gmail.com"
receiver_email = "bobbyestes68@gmail.com"
password = cod_kill_gmail #input("Type your password and press enter: ")
message = f"""\n
subject: Daily Weather Update

{api.city} weather is:

The sky is: {api.weather}
The wind speed is: {round(api.wind_speed)} mph
The temperature is: {round(api.temp * 1.8 - 459.67)}
    
This message was sent from Python."""

context = ssl.create_default_context() # Create a secure SSL context
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)  
