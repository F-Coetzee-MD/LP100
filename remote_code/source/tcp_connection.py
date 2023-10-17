import json
import socket

# Define the server"s address and port
server_address = "127.0.0.1"  # Replace with the server"s IP address
server_port = 12345  # Replace with the server"s port number

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  # Connect to the server
  client_socket.connect((server_address, server_port))

  # Send data to the server
  message = "Hello, server!"
  client_socket.send(message.encode("utf-8"))

  # Receive and print the server"s response
  response = client_socket.recv(1024)  # Adjust buffer size as needed
  print("Server Response: " + response.decode("utf-8"))

except Exception as e:
  print("An error occurred:", e)

finally:
  # Close the socket
  client_socket.close()
