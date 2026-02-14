# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
    serverSocket.bind(("", port))

# Fill in start
    serverSocket.listen(1)
# Fill in end
    print('The server is ready to receive')

    while True:
        print('Ready to serve..')

# Accept connections
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()

            filename = message.split()[1]
            file_path = filename[1:]

            # Read file as bytes
            f = open(file_path, 'rb')
            binary_data = f.read()

# 200 OK headers (ALL must use \r\n)
            header = "HTTP/1.1 200 OK\r\n"
            header += "Content-Type: text/html; charset=utf-8\r\n"
            header += "Content-Length: " + str(len(binary_data)) + "\r\n"
            header += "Server: ShiansServer\r\n"
            header += "\r\n"

            response = header.encode() + binary_data
            connectionSocket.sendall(response)

        except Exception:
            # 404 body (bytes)
            body = b"<html><body><h1>404 Not Found</h1></body></html>"

            header = "HTTP/1.1 404 Not Found\r\n"
            header += "Content-Type: text/html; charset=utf-8\r\n"
            header += "Content-Length: " + str(len(body)) + "\r\n"
            header += "Server: ShiansServer\r\n"
            header += "\r\n"

            response = header.encode() + body
            connectionSocket.sendall(response)

        # Close client socket
        connectionSocket.close()

if __name__ == "__main__":
    webServer(13331)

