from socket import *
import time                                             # DEBUG1: IMPORTED ONLY TO WAIT

def main():
    # Create a UDP socket
    # Notice the use of SOCK_DGRAM for UDP packets
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # To set waiting time of one second for reponse from server
    clientSocket.settimeout(1)

    for i in range(10):
        sendTime = time.time();
        message = 'PING ' + str(i + 1) + " " + str(time.strftime("%H:%M:%S"))
        address = ('127.0.0.1', 12000)
        clientSocket.sendto(message.encode(), address)

        try:
            data, server = clientSocket.recvfrom(1024)
            receivedTime = time.time()
            rtt = receivedTime - sendTime
            print("Message Received", data)
            print("RTT", rtt)
            print
        
        except timeout:
            print('Request Timed Out')
            print

if __name__ == '__main__':
    main()
