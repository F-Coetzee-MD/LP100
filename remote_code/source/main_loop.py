import sys
import time
import threading

from modbus_converter import modbus_maker
from usb_connection import usb_listener
from tcp_connection import tcp_client

usb_port = usb_listener()
modbus = modbus_maker()
client = tcp_client()

if __name__ == "__main__":
    while (True):
        # blocking code, will wait untill a message is received
        msg = usb_port.wait_for_pycan_message()
        print(msg)
        raw_data = usb_port.format_can_data(msg)

        # if data was received
        if(len(raw_data)):
            frame = modbus.create_new(raw_data, msg.arbitration_id)
            client.forward_message(frame)

        client.receive_response()
        

    
