# Python imports are like C's includes and Java's imports
import random
# You can random stuff

from socket import *
# This means that, import the "socket" package, 
# but we don't have to type "socket" everytime we use it
# 
# If we only did "import socket"
# We would have to do
# serverSocket = socket.socket(AF_INET, SOCK_DGRAM)
# 
# But if we used "from socket import *"
# We can just do
# serverSocket = socket(AF_INET, SOCK_DGRAM)
# 
# The from <something> import <alias> is usually used to give
# new names to stuff
# We can also do "from socket import socks"
# Then we can do
# serverSocket = socks.socket(AF_INET, SOCK_DGRAM)
# 
# It's there so we can avoid naming conflicts

import time                                             # DEBUG1: IMPORTED ONLY TO WAIT
# Used to get time lol
# The debug1 comments above is by sir
# You can just check the original one to see which are sir's comments


def main():
    # Create a UDP socket
    # Notice the use of SOCK_DGRAM for UDP packets
    # 
    # Sockets are basically like electrical sockets,
    # it's something that lets you connect two things
    # In this case, we're connecting the server and the client
    # 
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    # I don't know what AF_INET and SOCK_DGRAM means lol

    # Assign IP address and port number to socket
    serverSocket.bind(('127.0.0.1', 12000))

    while True:
        # Generate random number in the range of 0 to 10
        rand = random.randint(0, 10)
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        # Capitalize the message from the client
        message = message.upper()
        # If rand is less is than 4, we consider the packet lost and do not respond
        if rand < 4:
            continue
        # Otherwise, the server responds
        time.sleep(.05)              # DEBUG1: Wait only to simulate longer delay and test timeout large = more likely for timeout
        serverSocket.sendto(message, address)
    pass

if __name__ == '__main__':
    main()
