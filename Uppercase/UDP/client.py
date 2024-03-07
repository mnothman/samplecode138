#Client program to test socket programming using UDP. The client program defines server port and IP address of the server. The program sends lower case letters to the server and expect conversion to upper case letters. 
#usage : python3 client.py
# Find more documentation in https://realpython.com/python-sockets/

# Import the library 
from socket import *
# Define localhost information of domain name or IP address
serverName = 'localhost'
# Define the port information
serverPort = 12000
# Declare the file descriptor for the UDP socket
clientSocket = socket(AF_INET,SOCK_DGRAM)
# Get the message from the user input
message = input('Input lowercase sentence:')
# Send the encoded message to server with server name and port ID
clientSocket.sendto(message.encode(),(serverName, serverPort))
# Receive the modified message from the server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# Print the decoded message
print(modifiedMessage.decode())
# close the connection
clientSocket.close()