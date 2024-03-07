# Server program to create a TCP stream socket and start the server with arguments. 
# The server will accept arguments from the user as python <program name> < port number>
# Usage: python3 server.py <port number>
# Sample usage: python3 server.py 8001
# Find more documentation in https://realpython.com/python-sockets/

#Import libraries
import socket
import sys

# Define the function for creation of a server along with port numbers
def create_server(port):
    # Creating the file descriptor here
    svr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binding the port and the IP address of the host 
    svr_socket.bind(("0.0.0.0", port))
    # The server starts listening on ports 
    svr_socket.listen(1)

    print("Server listening on port :", port)
    
    # Opening a loop for clients to connect. Cliens may leave or connect at any time.
    while True:
        # the client is accepted and returns the socket descriptor as well as the address of 
        # the client.
        cli_socket, cli_address = svr_socket.accept()
        print("Accepted connection from", cli_address)

        # Do required operations of sending and receiving messages
        data = cli_socket.recv(1024)
        if data:
            print("Received from client:", {data.decode()})
            response = "Pong Response"
            print("Sending Pong")
            cli_socket.send(response.encode())
        cli_socket.close()
# The main function
def main():
    # In the main function, we need to check for length of the system arguments provided to run the program
    # If the number of argument mismatch, terminate the program
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        sys.exit(1)
    # You can take the port information of the provided argument and convert the string into integer
    port = int(sys.argv[1])
    # Start your server
    create_server(port)
    
# Run your script
if __name__ == "__main__":
    main()
