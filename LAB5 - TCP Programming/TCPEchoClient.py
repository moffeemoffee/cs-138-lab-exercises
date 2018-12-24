#!/usr/bin/env python3
'''
Illustrating a TCP client
'''

from socket import *
import sys

serverName = 'localhost'
serverPort = 12000

if len(sys.argv) == 3:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Input lowercase sentence: ")
clientSocket.send(bytes(sentence, "utf-8"))
modifiedSentence = clientSocket.recv(1024)
print("From server:", str(modifiedSentence,"utf-8"))
clientSocket.close()