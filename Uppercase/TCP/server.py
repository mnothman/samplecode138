#Server program to test socket programming using TCP. The server defines the port ID inside the program. The program accepts lowercase messages from the client, modifies them to uppercase message and send it back to the client. 
# Usage : python3 server.py
# Find more documentation in https://realpython.com/python-sockets/

#Import libraries
from socket import *

# declare server port
serverPort = 12000

#Declare a file descriptor for socket 
serverSocket = socket(AF_INET,SOCK_STREAM)

#Bind the socket to the serverport
serverSocket.bind(('',serverPort))

#Start listening on the server
serverSocket.listen(1)

print('The server is ready to receive')

while True:
# Accept connections from the clients returning the file descriptor and address of client
     connectionSocket, addr = serverSocket.accept()
# Receive decoded message from the client
     sentence = connectionSocket.recv(2048).decode()
# Modify the case of the word
     capitalizedSentence = sentence.upper()
# Send the modified encoded message to the client
     connectionSocket.send(capitalizedSentence.encode())
# Close the connection
     connectionSocket.close()
