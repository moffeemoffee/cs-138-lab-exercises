from socket import *
import time                                             # DEBUG1: IMPORTED ONLY TO WAIT

if __name__ == '__main__':
    # Create a UDP socket
    # Notice the use of SOCK_DGRAM for UDP packets
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # One second waiting time
    clientSocket.settimeout(1)

    for i in range(10):
        # Get send time to use later to check round trip time
        sendTime = time.time();

        # Make message
        message = 'Ping ' + str(i + 1)

        # Set IP address and port number
        address = ('127.0.0.1', 12000)
        clientSocket.sendto(message.encode(), address)

        try:
            data, server = clientSocket.recvfrom(1024)

            # Get received time
            receivedTime = time.time()

            # Calculate RTT
            rtt = receivedTime - sendTime
            print("Message Received", data)
            print("Round Trip Time", rtt)
            print
        
        except timeout:

            # Message wasn't returned (packet was dropped)
            print('Request Timed Out')
            print
