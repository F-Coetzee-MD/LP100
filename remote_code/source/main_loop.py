import sys
import time
import threading

from modbus_converter import modbus_maker
from usb_connection import usb_listener
from tcp_connection import tcp_client

main_loop_error = threading.Event()

def timeout_checker():
    while (True):
        main_loop_error.set()
        time.sleep(2)
        
        if (main_loop_error.is_set()):
            break
        elif KeyboardInterrupt:
            break

def main_loop():
    usb_port = usb_listener()
    modbus = modbus_maker()
    client = tcp_client()

    while (True):
        # blocking code, will wait untill a message is received
        msg = usb_port.wait_for_pycan_message()
        # print(msg)
        raw_data = usb_port.format_can_data(msg)

        # if data was received
        if(len(raw_data)):
            frame = modbus.create_new(raw_data, msg.arbitration_id)
            client.forward_message(frame)

        client.receive_response()
        main_loop_error.clear()

if __name__ == "__main__":
    process1 = threading.Thread(target = timeout_checker)
    process2 = threading.Thread(target = main_loop)

    process1.daemon = True
    process2.daemon = True

    process1.start()
    process2.start()

    process1.join()
    print("end it all")
    sys.exit()