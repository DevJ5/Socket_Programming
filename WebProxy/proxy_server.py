#!/usr/bin/python3
from socket import *
import sys
import traceback
import os

if len(sys.argv) < 1:
    print("Usage: proxy_server.py <server_ip>")
    sys.exit(2)

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverPort = 12000
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print("The server is ready to receive")

while True:
    clientSocket, addr = serverSocket.accept()
    try:
        print(f"Received connection from {addr}")
        message = clientSocket.recv(1024).decode()
        print(message)
        filename = message.split()[1][1:]
        print(filename)
        # Check if file exists in cache
        if os.path.isfile(filename):
            print("File exists on server")
            with open(filename, 'r') as f:
                outputData = f.readlines()

            print(outputData)
            clientSocket.send(b"HTTP/1.0 200 OK\r\n")
            clientSocket.send(b"Content-Type:text/html\r\n\r\n")
            for i in range(0, len(outputData)):
                clientSocket.send(outputData[i].encode("utf-8"))

        else:
            print("File does not exist on server")

        clientSocket.close()
        print("Finished...")
    except:
        print(traceback.format_exc())
