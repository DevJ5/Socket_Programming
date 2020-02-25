#!/usr/bin/python3
from socket import *
import datetime
for i in range (1, 11):
    try:
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        # Send a ping message to localhost:12000 using UDP
        start_time = datetime.datetime.now()
        request = f"Ping {i} {start_time}"
        clientSocket.sendto(bytes(request, 'utf-8'), ('localhost', 12000))
        # Wait 1 second, if no response => packet is lost
        clientSocket.settimeout(1)
        data, addr = clientSocket.recvfrom(1024)
        message = data.decode('utf-8')
        # Print the response message
        print(message)
        # Calculate the RTT in seconds
        end_time = datetime.datetime.now()
        RTT = end_time-start_time
        print(f"RTT: {RTT}")

    except error:
        print(f"Request {i} timed out")
