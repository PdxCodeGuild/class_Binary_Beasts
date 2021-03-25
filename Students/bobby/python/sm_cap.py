
import smtplib, ssl

port = 465 # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "code.killer1968@gmail.com"
receiver_email = "bobbyestes68@gmail.com"
password = input("Type your password and press enter: ")
message = """\n
subject: Hi there
    
This message was sent from Python."""

context = ssl.create_default_context() # Create a secure SSL context
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)  









  