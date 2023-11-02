import sys
import time
import threading

from modbus_converter import modbus_maker
from usb_connection import usb_listener
from tcp_connection import tcp_client

usb_port = usb_listener()
modbus = modbus_maker()
client = tcp_client()

main_loop_failed = None

def error_checker():
    main_loop_failed = True
    time.sleep(2)

    if (main_loop_failed):
        print("stopping application instance")
        usb_connection.close_connection()
        tcp_connection.close_connection()
        sys.exit()

def main_loop():
    while (True):
        # blocking code, will wait untill a message is received
        msg = usb_port.wait_for_pycan_message()
        raw_data = usb_port.format_can_data(msg)

        # if data was received
        if(len(raw_data)):
            frame = modbus.create_new(raw_data, msg.arbitration_id)
            client.forward_message(frame)

        # wait for response from drive (plc)
        #main_loop_failed = False

if __name__ == "__main__":
    print("starting application instance")
    thread1 = threading.Thread(target = main_loop)
    thread2 = threading.Thread(target = error_checker)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    
