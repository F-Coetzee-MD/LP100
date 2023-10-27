import json
import serial

from modbus_converter import modbus_maker
from tcp_connection import tcp_client

modbus = modbus_maker()
client = tcp_client()

file = open("./settings/communication.json", "r")
settings = json.load(file)

# define the  usb port's name and baudrate
usb_name = settings["can usb"]  
usb_baudrate = settings["usb baudrate"]  

# rather read COM port and baudrate from settings json file 
usb_port = serial.Serial(usb_name, baudrate = usb_baudrate) 

def close_usb_connection():
  usb_port.close()

def test_usb_connection():
  return True

def check_message_valid(msg):
  return True

def read_pycan_message():
  print()

if __name__ == "__main__":
  while(True):
    msg = read_pycan_message()

    # if all required data is present in the usb message
    if(check_message_valid(msg)):
      frame = modbus.create_new(msg)
      client.forward_message(frame)

    # if connection is not good to the can receiver
    if (not test_usb_connection()):
      close_usb_connection()
      break