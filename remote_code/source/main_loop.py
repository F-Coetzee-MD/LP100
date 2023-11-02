from modbus_converter import modbus_maker
from usb_connection import usb_listener
from tcp_connection import tcp_client

usb_port = usb_listener()
modbus = modbus_maker()
client = tcp_client()

if __name__ == "__main__":
  while(True):
    # blocking code, will wait untill a message is received
    msg = usb_port.wait_for_pycan_message()
    raw_data = usb_port.format_can_data(msg)

    # if data was received
    if(len(raw_data)):
      frame = modbus.create_new(raw_data, msg.arbitration_id)
      client.forward_message(frame)
    
    # if connection is not good to the controller
    # if (not client.test_connection()):
    #   client.close_usb_connection()
    #   usb_port.close_usb_connection()
    #   break

    # if connection is not good to the can receiver
    # if (not usb_port.test_usb_connection()):
    #   client.close_usb_connection()
    #   usb_port.close_usb_connection()
    #   break