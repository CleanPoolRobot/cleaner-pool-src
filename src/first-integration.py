#!/usr/bin/env python -u
import communication as s
import RPi.GPIO as GPIO
import time
import threads as threads
from threading import Thread
import pinout as pin
import sys, traceback
from Queue import Queue

pressure_two = 0
pressure_one = 0
CLOCKWISE = 1
COUNTER_CLOCKWISE = 0
def main():
  arduino = s.start_arduino()
  queue = Queue(maxsize=0)
  s.activate_pump(arduino)
  distance = Thread(target=threads.request_distance, args=(queue,arduino,'C'))
  distance.start()
  #time.sleep(1)
  while(1):
    #value = threads.request_distance(arduino,'C')
    value = queue.get()
    print value
    if(value  == '1'):
      print "entrei no if"
      s.deactive_pump(arduino)
      s.turn_servo_pump(360, CLOCKWISE)
      s.active_pump(arduino)
      time.sleep(5)
      break;
      
try:
    main()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
