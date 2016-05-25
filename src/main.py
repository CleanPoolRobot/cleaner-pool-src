import communication as s
import RPi.GPIO as GPIO
import time
pmw_dute = GPIO.PWM(11,50)
pmw_dute.start(5)

def turn_servo_pump(angle, direction):
  time_s = angle/270
  if (direction == 1):
      pmw_dute.ChangeDutyCycle(50)
      time.sleep(time_s)
  else:
      pmw_dute.ChangeDutyCycle(2.5)
      time.sleep(time_s)

  pmw_dute.ChangeDutyCycle(100)
  return

def main():
  while(1):
    s.activate_brush()
    time.sleep(1)
    s.deactive_brush()
    time.sleep(1)
  return
 
try:
    main()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
>>>>>>> Stashed changes
