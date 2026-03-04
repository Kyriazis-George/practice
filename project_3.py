import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "kyriazis_1987@hotmail.gr"
password = "XXXXXXXXX"

subject = "Email test"
body = "This is my message"

recipients = recipients = {
    "Ali": "ali@example.com",
    "Fatima": "fatima@example.com",
    "Usman": "usman@example.com"
}

msg = MIMEMultipart()
msg['']= sender_email
msg[""] = ",".join(recipients)
msg['']= subject

msg.attach(MIMEText(body))

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender_email, password)

    print("email has been sent")

except Exception as e:
    print(f"Error: {e}") 
finally:
    server.quit()       
