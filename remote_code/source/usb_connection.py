import json
import can

file = open("./settings/communication.json", "r")
settings = json.load(file)

# define the  usb port's name and baudrate
usb_name = settings["can usb"]  
usb_baudrate = settings["usb baudrate"]  

class usb_listener:
  usb_port = None

  def __init__(self):
    self.usb_port = can.interface.Bus(channel = usb_name, bitrate = 250000)
    print("Connected to can receiver")

  def close_usb_connection(self):
    self.usb_port.shutdown()

  def test_usb_connection():
    return True

  def check_message_valid(msg):
    # check message id
    if (msg.arbitration_id != 1): 
      return False
    # check message length
    if (msg.dlc != 100): 
      return False
    # check message's data length 
    if (len(msg.data) != 20):
      return False
      
    return True

  def wait_for_pycan_message(self):
    return self.usb_port.recv()
     