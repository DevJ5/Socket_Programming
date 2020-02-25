#!/usr/bin/python3
from socket import *
import ssl
import base64

emailaddress = ""
emailaddressto = ""
emailpassword = ""
encoding = "utf-8"

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
mailserver = "smtp.gmail.com"
port = 587

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
recv = clientSocket.recv(1024).decode()

if recv[:3] != "220":
    print("220 reply not received from server.")

heloCommand = "Helo Google\r\n"
clientSocket.send(bytes(heloCommand, "UTF-8"))
recv1 = clientSocket.recv(1024).decode()
if recv1[:3] != "250":
    print("250 replay not received from server.")

startsslCommand = "STARTTLS\r\n"
clientSocket.send(startsslCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
context = ssl.create_default_context()
secureClientSocket = context.wrap_socket(clientSocket, server_hostname = mailserver)
authCommand = "AUTH LOGIN\r\n"
secureClientSocket.send(authCommand.encode())
recv3 = secureClientSocket.recv(1024).decode()
print(recv3)
username = base64.b64encode(bytes(emailaddress, encoding))
usernameCommand = username + b"\r\n"
secureClientSocket.send(usernameCommand)
recv4 = secureClientSocket.recv(1024).decode()
print(recv4)
password = base64.b64encode(bytes(emailpassword, encoding))
passwordCommand = password + b"\r\n"
secureClientSocket.send(passwordCommand)
recv5 = secureClientSocket.recv(1024).decode()
print(recv5)
mailfromCommand = bytes(f"MAIL FROM: <{emailaddress}>\r\n", encoding)
secureClientSocket.send(mailfromCommand)
recv6 = secureClientSocket.recv(1024).decode()
print(recv6)
recepientCommand = bytes(f"RCPT TO: <{emailaddressto}>\r\n", encoding)
secureClientSocket.send(recepientCommand)
recv7 = secureClientSocket.recv(1024).decode()
print(recv7)
dataCommand = "DATA\r\n"
secureClientSocket.send(dataCommand.encode())
recv8 = secureClientSocket.recv(1024).decode()
print(recv8)
secureClientSocket.send(b"Hola from Espana!\r\n")
secureClientSocket.send(b".\r\n")
recv9 = secureClientSocket.recv(1024).decode()
print(recv9)
secureClientSocket.send("QUIT\r\n".encode())
recv10 = secureClientSocket.recv(1024).decode()
print(recv10)

