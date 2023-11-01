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

class usb_listener:
  usb_port = None

  def __init__(self):
    self.usb_port = can.interface.Bus(channel = usb_name, bitrate = usb_baudrate)
    print("Connected to can receiver")

  def close_usb_connection(self):
    self.usb_port.shutdown()

  def test_usb_connection():
    return True

  def check_message_valid(msg, type):
    # check message id

    # check message length
    if (msg.dlc != can_total_size): 
      return False

    # check message's data length 
    if (len(msg.data) != can_data_size):
      return False
      
    return True

  def format_can_data(self, can_msg):
    can_data = can_msg.data
    formatted_data = []

    # analog joystick data
    if (can_data.arbitration_id == can_settings["analog frame"]["id"]):  
      self.check_message_valid(can_msg, "analog frame")

    # digital button values
    elif (can_data.arbitration_id == can_settings["digital frame"]["id"]):
      self.check_message_valid(can_msg, "digital frame")

    return formatted_data

  def wait_for_pycan_message(self):
    return self.usb_port.recv()
     