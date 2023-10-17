import serial

# Replace "COMx" with the actual COM port where your USB device is connected
ser = serial.Serial("COMx", baudrate=9600)  # Adjust the baud rate as needed

try:
  while True:
    message = ser.readline().decode("utf-8")
    print("Received: " + message, end="")
except KeyboardInterrupt:
  print("Exiting...")
finally:
  ser.close()