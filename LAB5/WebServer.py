from socket import *

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 80))
    serverSocket.listen(1)

    while True:
        print('WebServer on\n')
        connSocket, addr = serverSocket.accept()

        try:
            message = connSocket.recv(1024)
            print('Message:', message)

            fileName = message.split()[1]
            print('File name:', fileName)
            file = open(fileName[1:])

            outputData = file.read()
            print('Output data:', outputData)

            connSocket.send(b'\n')
            connSocket.send(b'HTTP/1.1 200 OK\n')
            connSocket.send(b'Connection: close\n')

            contentLen = len(outputData)
            contentLenStr = 'Content-Length: ' + str(contentLen) + '\n'
            connSocket.send(contentLenStr.encode())
            connSocket.send(b'Content-Type: text/html\n')
            connSocket.send(b'\n')
            connSocket.send(b'\n')

            for i in range(0, contentLen):
                connSocket.send(outputData[i].encode())

        except IOError:
            print('IOError')
            connSocket.send(b'\n')
            connSocket.send(b'404 Not Found')

        connSocket.close();

    serverSocket.close()
    pass

if __name__ == '__main__':
    main()