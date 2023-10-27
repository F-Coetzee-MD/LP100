import json

from tcp_connection import tcp_client

def to_word(integer):
  msb = (integer>>8)&0xff
  lsb = integer&0xff
  return [msb, lsb]

def to_byte(integer):
  return [integer]

class modbus_maker:
  def __init__(self):
    self.overheads = []
    file = open("./settings/modbus_frame.json", "r")
    json_frame = json.load(file)
    self.overheads += to_word(json_frame["transaction id"])
    self.overheads += to_word(json_frame["protocol id"])
    self.overheads += to_word(json_frame["length"])
    self.overheads += to_byte(json_frame["unit code"])
    self.overheads += to_byte(json_frame["function code"])
    self.overheads += to_word(json_frame["register"])
    self.overheads += to_word(json_frame["register count"])
    self.overheads += to_byte(json_frame["byte count"])
    file.close()

  def create_new(self, can_data):
    data = []
    for value in can_data:
      data += to_word(value)
    return self.overheads + data

# used for testing, remove later

modbus = modbus_maker()

for x in range(10):
  print(modbus.create_new([1,2,3,4,5]))


