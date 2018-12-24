#!/usr/bin/env python3

'''
Illustrating a TCP server
'''

from socket import *
import sys

serverPort = 12000
if len(sys.argv) == 2:
    serverPort = int(sys.argv[1])

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    print(addr, "connected...")
    sentence = connectionSocket.recv(1024)
    print("Message sent by", connectionSocket.getpeername(), "to", connectionSocket.getsockname(), ":",
          str(sentence, "utf-8"))
    capitalizedSentence = str(sentence, "utf-8").upper()
    connectionSocket.send(bytes(capitalizedSentence, "utf-8"))
    connectionSocket.close()