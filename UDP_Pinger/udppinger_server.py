#!/usr/bin/python3
import random
from socket import *

# Create UDP Socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("Server listening on port: 12000")
while True:
    rand = random.randint(0,10)
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    if rand < 4:
        continue
    serverSocket.sendto(message, address)
