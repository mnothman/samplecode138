# A simple client-server program to demonstrate the ability of a server to perform computations
# This is the server side code. The client will supply the numbers and the operations such as add, subtract, multiply and divide. 
# Usage: python3 server.py <port no.>
# Same usage: python3 server.py 8001
# Find more documentation in https://realpython.com/python-sockets/

# Import libraries
import socket
import sys

# Define the following functions with arguments as operations of add, multiply, subtract and divide 
# Additionally, also mention the two numbers that you want to perform the computations for.
def perform_operation(op, num1, num2):
    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Define the starting of server similar to what you have seen in the argument folder programs
# All the comments are not mentioned to avoid duplication
def start_server(port):
    # Define the socket descriptor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Define the host
    host = '0.0.0.0'
    # Bind the server
    server_socket.bind((host, port))
    # Listen for new connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    # Start the while loop
    while True:
        # Accept the connection with socekt descriptor and address of remote client
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        # Seperating the data using split(',')
        operation, num1, num2 = data.split(',')
        num1, num2 = int(num1), int(num2)
        # Perform the desired operations
        result = perform_operation(operation, num1, num2)
        client_socket.send(str(result).encode('utf-8'))
        # Close the socket
        client_socket.close()

# Define the main function to accept the 2 arguments
def main():
    # Check for number of arguments or print the usage information
    if len(sys.argv)!=2:
        print("Usage: python3 server.py <port no.>" )
        sys.exit(1)
    # convert the string format of port to integer
    port = int(sys.argv[1])
    # start the server
    start_server(port)
    
# Run the script
if __name__ == "__main__":
    main()
