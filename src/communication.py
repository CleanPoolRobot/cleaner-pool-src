import pinout
import time
import serial
import RPi.GPIO as GPIO
import time 
#Configura a serial e a velocidade de transmissao
#pmw=GPIO.PWM(pinout.SERVO_WHEELS,50)
#pmw.start(5)

pmw_dute = GPIO.PWM(pinout.SERVO_PUMP,50)
pmw_dute.start(5) 
def start_arduino():
    arduino_communication = serial.Serial("/dev/ttyAMA0", 115200)
    return arduino_communication

def read_arduino(arduino_communication):
    response = arduino_communication.readline()
    return response     

def write_arduino(arduino_communication, line):
    arduino_communication.write(line)
    return

def activate_pump():
    GPIO.output(WATER_PUMP, GPIO.HIGH)
    return true

def deactive_pump():
    GPIO.output(WATER_PUMP, GPIO.LOW)
    return false

def turn_servos_wheels(angle):
    duty = float(angle)/20 + 2.5
    pmw.ChangeDutyCycle(duty)      
    return

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

