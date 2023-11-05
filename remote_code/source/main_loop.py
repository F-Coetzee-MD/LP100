import sys
import time
from multiprocessing import Process, Value
from modbus_converter import modbus_maker
from usb_connection import usb_listener
from tcp_connection import tcp_client

main_loop_error = Value('b', False)

usb_port = usb_listener()
modbus = modbus_maker()
client = tcp_client()

def timeout_checker():
    while (not main_loop_error):
        with main_loop_error.get_lock():
            main_loop_error.value = True

        time.sleep(2)

def main_loop():
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

        with main_loop_error.get_lock():
            main_loop_error.value = False

if __name__ == "__main__":
    process1 = Process(target = timeout_checker)
    process2 = Process(target = main_loop)

    process1.start()
    process2.start()

    process1.join()
    sys.exit()
    
"""
import multiprocessing

class SharedClass:
    def __init__(self, value):
        self.value = value

def modify_shared_object(shared_object):
    shared_object.value += 1

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    shared_instance = manager.Namespace()
    shared_instance.my_class = SharedClass(0)

    process1 = multiprocessing.Process(target=modify_shared_object, args=(shared_instance.my_class,))
    process2 = multiprocessing.Process(target=modify_shared_object, args=(shared_instance.my_class,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Shared object value:", shared_instance.my_class.value)
"""


"""
import multiprocessing
import time

class SharedClass:
    def __init__(self):
        self.value = 0
        self.lock = multiprocessing.Lock()  # Create a lock

    def increment(self):
        with self.lock:
            self.value += 1

def worker(shared_instance):
    for _ in range(3):
        shared_instance.increment()
        time.sleep(1)

if __name__ == "__main__":
    shared_instance = SharedClass()

    process1 = multiprocessing.Process(target=worker, args=(shared_instance,))
    process2 = multiprocessing.Process(target=worker, args=(shared_instance,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Shared object value:", shared_instance.value)
"""

"""
import multiprocessing

main_loop_error = 0

def increment_error():
    global main_loop_error
    main_loop_error += 1

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=increment_error)
    process2 = multiprocessing.Process(target=increment_error)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Main loop error count:", main_loop_error)
"""

    
