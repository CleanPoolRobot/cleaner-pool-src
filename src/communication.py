import pinout
import time
import serial
 
#Configura a serial e a velocidade de transmissao
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
    return

def deactive_pump():
    GPIO.output(WATER_PUMP, GPIO.LOW)
    return
        
while(1):
    #Verifica se o botao foi pressionad
    #Envia o caracter L pela serial
    arduino_communication = start_arduino
    arduino_communication.write("L")
    print("Enviado - L")
    #Aguarda reposta
    resposta = arduino_communication.readline()
    #Mostra na tela a resposta enviada
    #pelo Arduino
    print resposta
    #Aguarda 0,5 segundos e reinicia o processo
    time.sleep(0.5)


