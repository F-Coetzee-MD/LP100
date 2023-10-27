import json
import socket

file = open("./settings/communication.json", "r")
settings = json.load(file)

# define the server"s address and port
server_address = settings["tcp ip"]  
server_port = settings["tcp port"]  

class tcp_client:
  # create a socket object
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def __init__(self):
    # connect to the server
    self.client_socket.connect((server_address, server_port))

  def forward_message(self, modbus_frame):
    # send data to the server
    self.client_socket.sendall(bytes(modbus_frame))

  def close_connection(self):
    # close the socket
    self.client_socket.close()