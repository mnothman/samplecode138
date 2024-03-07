# Client program to test socket programming using TCP. The client program defines server port and IP address of the server. The program sends lower case letters to the server and expect conversion to upper case letters. 
# usage : python3 client.py
# Find more documentation in https://realpython.com/python-sockets/

#Import libraries
from socket import *

# Declare server hostname
serverName = 'localhost'

# Declare server port number 
serverPort = 12000

# Create the file descriptor for socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server 
clientSocket.connect((serverName,serverPort))

# Take input from the user
sentence = input('Input lowercase sentence:')

# Send the encoded message to the server
clientSocket.send(sentence.encode())

# Receive the message from the server
modifiedSentence = clientSocket.recv(2048)

# Display the decoded message
print ('From Server:', modifiedSentence.decode())

# Close the socket or file descriptor 
clientSocket.close()
