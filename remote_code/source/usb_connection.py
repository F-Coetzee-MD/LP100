import json
import serial

def check_is_frame_valid():
  print()

# rather read COM port and baudrate from settings json file 

ser = serial.Serial("COMx", baudrate=9600) 

try:
  while True:
    message = ser.readline().decode("utf-8")
    print("Received: " + message, end="")
except KeyboardInterrupt:
  print("Exiting...")
finally:
  ser.close()