import thread
import communication as com

semaphore = thread.allocate_lock()

def request_distance(distance, arduino_communication, request_type)
  while True:
    semaphore.acquire()
    com.write_arduino(arduino_communication,request_type)
    distance = com.read_arduino(arduino_communication)
    semaphore.release()
  return distance

def request_pressure(pressure, arduino_communication, request_type)
  while True:
    semaphore.acquire()
    com.write_arduino(arduino_communication,request_type)
    pressure = com.read_arduino(arduino_communication)
    semaphore.release()
  return pressure
         
  

