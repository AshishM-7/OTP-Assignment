# OTP to mail

import smtplib
import random

sender = "ashish204magar@gmail.com"
password = "gvkguusgyahnhnfe"
receiver = "ashish204magar@gmail.com"
body = "Your OTP is " + str(random.randint(100000, 999999)) + ". Valid for next 15 minutes."

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender, password)

server.sendmail(sender, receiver, body)

print("Mail sent")