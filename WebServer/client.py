#!/usr/bin/python3
import sys
import socket
if len(sys.argv) != 4:
    print(f"Incorrect input: Format <script.py> <server_host> <server_port> <filename>")
try:
    host, port, filename = sys.argv[1:]
    print(host, port, filename)

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host, int(port)))
    clientSocket.send(b"GET /" + filename.encode())
    message = clientSocket.recv(1024)
    print("From server: ", message)
    clientSocket.close()
except:
    print("Couldn't connect to server...")
