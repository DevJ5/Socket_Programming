#!/usr/bin/python3
import socket
import threading
import traceback
import time

class ThreadedServer(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        self.serverSocket.bind((self.hostname, self.port))
        self.threads = []

    def listen(self):
        self.serverSocket.listen(2)
        print(f"Server listening on port {self.port}")
        while True:
            connectionSocket, address = self.serverSocket.accept()
            print(f"connection incoming {address}")
            new_thread = threading.Thread(target = self.listenToClient, args = (connectionSocket, address))
            new_thread.start()
            self.threads.append(new_thread)

    def listenToClient(self, connectionSocket, address):
        print("Listening to client invoked")
        size = 1024
        try:
            # data is now a bytestring
            data = connectionSocket.recv(size)
            # Decode the byestring into a normal request message
            message = data.decode()
            print(message)
            filename = message.split()[1]
            with open(filename[1:], "r") as f:
                outputdata = f.read()
                connectionSocket.send(b"HTTP/1.0 200 OK\r\n")
                connectionSocket.send(b"Content-Type: text/html\r\n\r\n")
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode('utf8'))
            time.sleep(5)
            connectionSocket.close()
        except IOError:
            connectionSocket.send(b"HTTP/1.0 404 NOT FOUND\r\n")
            connectionSocket.send(b"Content-Type: text/html\r\n\r\n")
            connectionSocket.send(b"<html><body><h1>404 Not Found</h1></body></html>")
            connectionSocket.close()
            return False
        except:
            print(traceback.format_exc())
            connectionSocket.close()


if __name__ == "__main__":
    ThreadedServer('', 12000).listen()
