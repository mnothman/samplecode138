# Server program for testing socket programming using UDP.The server defines the port ID inside the program. The program accepts lowercase messages from the client, modifies them to uppercase message and send it back to the client.  
# usage : python3 server.py
# Find more documentation in https://realpython.com/python-sockets/

#Import library
from socket import *
#Declare the server port
serverPort = 12000
#Declare the socket descriptor for UDP 
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Bind socket to IP address and port information
serverSocket.bind(('0.0.0.0', serverPort))

print('The server is ready to receive')
while True:
    # Receive message and client address from
    message, clientAddress = serverSocket.recvfrom(2048)
    # Modify the message
    modifiedMessage = message.decode().upper()
    # Send message to the client
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
    
