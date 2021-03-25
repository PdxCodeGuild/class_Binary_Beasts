import smtplib, ssl
import getpass

port = 465
smtp_server = "smtp.gmail.com"
sender_email = 'codersontesting@gmail.com'
receiver_email = 'seanwilcox@comcast.net'
pw = input("Enter your password: ")
message = """
    Subject: Hello, Sean.

    This message is your homework."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, pw)
    server.sendmail(sender_email, receiver_email, message)
