from serialrw import serial_rw
import numpy as np
class GPS_tracker:
  def __init__(self, file_name="gps_data.txt"):
    self.Serial = serial_rw()
    self.file_name = file_name
  def read_coords(self):
    f = open(self.file_name, "w")
    coords = np.array([])
    for i in range(0, 20):
      f.write(self.Serial.serial_read_line())
    f.close()
    f = open(self.file_name, "r")
    for line in f.readlines():
      line_split = line.split(",")
      j = 0
      for word in line_split:
        if word == "$GNGLL":
          coords = np.append(coords, (line_split[j+1][0]+line_split[j+1][1]))
          coords = np.append(coords, (line_split[j+1][2]+line_split[j+1][3]))
          #conversion from fraction part of minute to seconds
          coords = np.append(coords, str(float((float(line_split[j+1][5]+line_split[j+1][6]+line_split[j+1][7]+line_split[j+1][8])
          *60)/10000)))
          coords = np .append(coords, line_split[j+2])
          coords = np.append(coords, (line_split[j+3][0]+line_split[j+3][1]+line_split[j+3][2]))
          coords = np.append(coords, (line_split[j+3][3]+line_split[j+3][4]))
          #conversion from fraction part of minute to seconds
          coords = np.append(coords, str(float((float(line_split[j+3][6]+line_split[j+3][7]+line_split[j+3][8]+line_split[j+3][9])
          *60)/10000)))
          coords = np .append(coords, line_split[j+4])
          return coords
        j += 1
          
