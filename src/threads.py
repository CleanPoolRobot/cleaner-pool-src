#!/usr/bin/env python -u
import thread
import communication as com
import time
semaphore = thread.allocate_lock()
def request_distance(queue, arduino_communication, request_type):
  while True:
    semaphore.acquire()
    distance = 0
    com.write_arduino(arduino_communication,request_type)
    time.sleep(0.1)
    distance = com.read_arduino(arduino_communication)
    queue.put(distance)
    time.sleep(0.1)
    semaphore.release()
  return distance

def request_pressure(queue, arduino_communication, request_type):
  while True:
    semaphore.acquire()
    #print "Requisitando pressao - " + request_type
    com.write_arduino(arduino_communication,request_type)
    time.sleep(0.05)
    pressure = com.read_arduino(arduino_communication)
    queue.put(pressure)
    semaphore.release()
  return
         
  

