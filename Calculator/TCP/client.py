# A simple client-server program to demonstrate the ability of a server to perform computations
# This is the client program
# The client will supply the numbers and the operations such as add, subtract, multiply and divide
# information provided by the client. 
# Usage: python3 client.py <host/IP> <port ID> <operation add/subtract> <number 1> <number 2> 
# Sample usage : python3 client.py ecs-coding1.csus.edu 8001 add 10 20
# Find more documentation in https://realpython.com/python-sockets/

import socket
import sys

# Defining the client information to be sent over the network, the data consists of all the information 
# about the operation and the numbers
def client_inputs(data, host, port):
    # Declare the socket descriptor for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server and port
    client_socket.connect((host, port))
    # Send the data to the server
    client_socket.send(data.encode('utf-8'))
    # Receive the data from the server
    result = client_socket.recv(1024).decode('utf-8')
    # Print results
    print(f"Result from server: {result}")
    # Close the connection
    client_socket.close()

# define the main function to perform the computations
if __name__ == "__main__":
    # Check if the client provided six arguments, else print the usage command
    if len(sys.argv) != 6:
        print("Usage: python client.py <server/host> <port> <operation> <num1> <num2>")
        sys.exit(1)
    # Get the host information
    host = sys.argv[1]
    # Get the port information 
    port = int(sys.argv[2])
    # Define the operations
    operation = sys.argv[3]
    # Define the first number
    num1 = int(sys.argv[4])
    # Define the second number
    num2 = int(sys.argv[5])

    data = f"{operation},{num1},{num2}"
    #Run the client function to connect to server
    client_inputs(data, host, port)


