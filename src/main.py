import communication as s
import RPi.GPIO as GPIO
import time
import threads
import thread
import pinout as pin

pressure_two = 0
pressure_one = 0
def main():
  #s.turn_servo_pump(90,1)
  s.turn_servos_wheels(0)
  #pwm_dute.ChangeDutyCycle(100)
try:
    main()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
