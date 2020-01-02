import serial
from time import sleep

class serial_rw:
  def __init__(self, baud_rate = 115200, time_out=-1):
    self.port = serial.Serial("/dev/ttyS0", baudrate=baud_rate)
   def serial_read_line(self):
    return self.port.readline()
   def serial_read_char(self):
    return self.port.read()
   def serial_write(self, text="hi\n"):
    self.port.write(text)
   def serial_close(self):
    self.port.close()
    
