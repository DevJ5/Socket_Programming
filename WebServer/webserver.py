#!/usr/bin/python3
import traceback
from socket import *
import time

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Prepare a server socket
serverPort = 12000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        # Get client's ip and port number
        ip, port = connectionSocket.getpeername()
        print(f"Client socket: {ip}:{port}")
        # Get request message
        message = connectionSocket.recv(1024).decode()
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        # Send one HTTP header line into the socket
        connectionSocket.send(b"HTTP/1.0 200 OK\r\n")
        connectionSocket.send(b"Content-Type: text/html\r\n\r\n")
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf8'))
        time.sleep(5)
        connectionSocket.close()
        print("Finished...")
    except IOError:
        connectionSocket.send(b"HTTP/1.0 404 Not Found\r\n")
        connectionSocket.send(b"Content-Type: text/html\r\n\r\n")
        connectionSocket.sendall(b"<html><head></head><body><h1>404 Not Found</h1></body></html>")
        connectionSocket.close()
    except:
        print(traceback.format_exc())

serverSocket.close()
