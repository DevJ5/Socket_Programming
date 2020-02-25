#!/usr/bin/python3
import smtplib
sender=''
receiver=''
password=''
smtpserver=smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(sender,password)
msg="""From: Ayushi
To: Ruchi
MIME-Version: 1.0
Content-type: text/html
Subject:Demo
This is a demo<br/><p align="center">Hi</p><hr/>"""
smtpserver.sendmail(sender,receiver,msg)
print('Sent')
smtpserver.close()
