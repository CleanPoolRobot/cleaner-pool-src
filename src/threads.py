import thread
import communication as com

def request_distance(distance, arduino_communication, request_type)
  com.write_arduino(arduino_communication,request_type)
  distance = com.read_arduino(arduino_communication)
  return distance

def request_pressure(pressure, arduino_communication, request_type)
  com.write_arduino(arduino_communication,request_type)
  pressure = com.read_arduino(arduino_communication)
  return pressure
         
  

