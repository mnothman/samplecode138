
# Client program to send a request of ping and get a response on pong 
# The client will get arguments from the user as python <program name> <hostname> < port number>
# Usage : python3 client.py <server-name> <port>
# Sample usage: python3 client.py ecs-coding1.csus.edu 8001
# Find more documentation in https://realpython.com/python-sockets/

#Import libraries
import socket
import sys

# Define the function for creation of a client
def create_client(svr_ip, svr_port):
    # You are create the file descriptor here
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server ip address and the port information that you declared in yuor arguments
    cli_socket.connect((svr_ip, svr_port))

    # Communicate with the server here (e.g., send/receive data)
    message = "Hello, This is the client requesting Ping"
    cli_socket.send(message.encode())

    response = cli_socket.recv(1024)
    if response:
        print(f"Received from server: {response.decode()}")
    cli_socket.close()
    
# Define the main function 
def main():
    # Check for arguments, if valid number of arguments, then accept, or else reject
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)
    # Separate the strings of IP address and Port informartion
    # Notice that server IP is in string format, but the port is in integer format
    svr_ip = sys.argv[1]
    svr_port = int(sys.argv[2])
    # start the client
    create_client(svr_ip, svr_port)

# Run your script
if __name__ == "__main__":
    main()
