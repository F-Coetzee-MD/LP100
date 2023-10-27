import json
import serial

file = open("./settings/communication.json", "r")
settings = json.load(file)

# define the  usb port's name and baudrate
usb_name = settings["can usb"]  
usb_baudrate = settings["usb baudrate"]  

class usb_listener:
  usb_port = None

  def __init__(self):
    self.usb_port = serial.Serial(usb_name, baudrate = usb_baudrate)

  def close_usb_connection(self):
    self.usb_port.close()

  def test_usb_connection():
    return True

  def extract_data():
    data = []
    # extract data from the usb message frame

    return data

  def check_message_valid(msg):
    # check to make sure a valid frame was received
    # if not terun false, else, return true
    return True

  def read_pycan_message(self):
    message = []
    # wait for message to be received on the usb port
    # format message to be list format

    return message