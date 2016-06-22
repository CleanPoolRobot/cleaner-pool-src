#!/usr/bin/env python -u
import pinout as pin
import time
import serial
import RPi.GPIO as GPIO
import time 
#Configura a serial e a velocidade de transmissao
pwm=GPIO.PWM(pin.SERVO_WHEELS,50)
pwm.start(5)

pwm_dute = GPIO.PWM(pin.SERVO_PUMP,50)
pwm_dute.start(5) 

def start_arduino():
    arduino_communication = serial.Serial("/dev/ttyAMA0", 115200)
    return arduino_communication

def read_arduino(arduino_communication):
    #print "esperando resposta"
    response = arduino_communication.read()
    print response
    return response     

def write_arduino(arduino_communication, line):
    arduino_communication.write(line)
    return

def activate_pump(arduino_communication):
   write_arduino(arduino_communication, 'G')
   time.sleep(0.1)
   #read_arduino(arduino_communication) 
   return True

def deactive_pump(arduino_communication):
    write_arduino(arduino_communication, 'H')
    time.sleep(3)
    #read_arduino(arduino_communication)
    return False

def activate_brush():
    GPIO.output(pin.BRUSH, GPIO.HIGH)
    return True

def deactive_brush():
    GPIO.output(pin.BRUSH, GPIO.LOW)
    return False

def turn_servos_wheels(angle):
    duty = float(angle)/20 + 2.5
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.8)      
    return

def turn_servo_pump(angle, direction):
    if (direction == 1):
      if angle == 0:
        teste = 0
      elif (angle == 90):
        pwm_dute.ChangeDutyCycle(50)
        time.sleep(1.71)
      elif angle == 180:
        pwm_dute.ChangeDutyCycle(50)
        time.sleep(0.74)
      elif angle == 270:
        pwm_dute.ChangeDutyCycle(50)
        time.sleep(1.1)
      else:
        pwm_dute.ChangeDutyCycle(50)
        time.sleep(6.5)
    else:
      if angle == 0:
        pwm_dute.ChangeDutyCycle(2.5)
        time.sleep(0)
      elif angle == 90:
        pwm_dute.ChangeDutyCycle(2.5)
        time.sleep(0.24)
      elif angle == 180:
        pwm_dute.ChangeDutyCycle(2.5)
        time.sleep(0.54)
      elif angle == 270:
        pwm_dute.ChangeDutyCycle(2.5)
        time.sleep(0.905)
      else:
        pwm_dute.ChangeDutyCycle(2.5)
        time.sleep(1.2)
   
    pwm_dute.ChangeDutyCycle(100) 
    return
     
#while(1):
    #Verifica se o botao foi pressionad
    #Envia o caracter L pela serial
   # arduino_communication = start_arduino()
   # arduino_communication.write("L")
   # print("Enviado - L")
    #Aguarda reposta
    #resposta = arduino_communication.readline()
    #Mostra na tela a resposta enviada
    #pelo Arduino
   # print resposta
    #Aguarda 0,5 segundos e reinicia o processo
    #time.sleep(0.5)

