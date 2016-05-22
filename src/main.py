import communication
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
  cont = 0
  time_s = 90/270
   #communication.turn_servos_wheels(0)
  while(cont <=1):
     pmw_dute.ChangeDutyCycle(50)
     time.sleep()
     pmw_dute.ChangeDutyCycle(100)
  # communication.turn_servo_pump(90,0)
     cont+1
  return
 
main()
