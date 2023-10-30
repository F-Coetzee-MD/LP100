from modbus_converter import modbus_maker
from usb_connection import usb_listener
from tcp_connection import tcp_client

usb_port = usb_listener()
modbus = modbus_maker()
client = tcp_client()

if __name__ == "__main__":
  while(True):
    # blocking code, will wait untill a message is received
    msg = usb_port.read_pycan_message()

    # if all required data is present in the usb message
    if(usb_port.check_message_valid(msg)):
      data = usb_port.extract_data(msg)
      frame = modbus.create_new(msg.data)
      client.forward_message(frame)
    
    # if connection is not good to the controller
    if (not client.test_usb_connection()):
      client.close_usb_connection()
      usb_port.close_usb_connection()
      break

    # if connection is not good to the can receiver
    if (not usb_port.test_usb_connection()):
      client.close_usb_connection()
      usb_port.close_usb_connection()
      break