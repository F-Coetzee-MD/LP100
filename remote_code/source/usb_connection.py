import json
import can

file = open("./settings/communication.json", "r")
settings = json.load(file)

file = open("./settings/can_frame.json", "r")
can_settings = json.load(file)

file.close()

# define the  usb port's name and baudrate
usb_name = settings["can usb"]  
usb_baudrate = settings["usb baudrate"]  

# incoming can bus frame settings
can_id = can_settings["frame id"]
can_data_size = can_settings["data size"]
can_total_size = can_settings["frame size"]

class usb_listener:
  usb_port = None

  def __init__(self):
    self.usb_port = can.interface.Bus(channel = usb_name, bitrate = usb_baudrate)
    print("Connected to can receiver")

  def close_usb_connection(self):
    self.usb_port.shutdown()

  def test_usb_connection():
    return True

  def check_message_valid(msg):
    # check message id
    if (msg.arbitration_id != can_id): 
      return False

    # check message length
    if (msg.dlc != can_total_size): 
      return False

    # check message's data length 
    if (len(msg.data) != can_data_size):
      return False
      
    return True

  def wait_for_pycan_message(self):
    return self.usb_port.recv()
     