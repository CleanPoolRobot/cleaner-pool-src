import RPi.GPIO as GPIO

MUX_ENGINE = 11;

BRIDGE_H0_ENGINE = 13;
BRIDGE_H1_ENGINE = 15;

WATER_PUMP = 12;

AG_SDA1_I2C = 3;
AG_SCL1_I2C = 5;

GPIO.setup(MUX_ENGINE,GPIO.OUT)
GPIO.setup(BRIDGE_H0_ENGINE,GPIO.OUT)
GPIO.setup(BRDIGE_H1_ENGINE,GPIO.OUT)
GPIO.setup(WATER_PUMP, GPIO.OUT)
GPIO.setup(AG_SDA1_12C, GPIO.IN)
GPIO.setup(AG_SCL1_12C, GPIO.IN)