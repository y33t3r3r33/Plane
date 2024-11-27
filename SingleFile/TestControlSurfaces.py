import RPi.GPIO as GPIO
from time import sleep

FI1 = 23
FI2 = 24
FE1 = 25

AI1 = 21
AI2 = 22
AE1 = 20

EI1 = 08
EI2 = 09
EE1 = 07

RI1 = 12
RI2 = 11
RE1 = 10

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FI1, GPIO.OUT)
    GPIO.setup(FI2, GPIO.OUT)
    GPIO.setup(FE1, GPIO.OUT)
    GPIO.setup(AI1, GPIO.OUT)
    GPIO.setup(AI2, GPIO.OUT)
    GPIO.setup(AE1, GPIO.OUT)
    GPIO.setup(EI1, GPIO.OUT)
    GPIO.setup(EI2, GPIO.OUT)
    GPIO.setup(EE1, GPIO.OUT)
    GPIO.setup(RI1, GPIO.OUT)
    GPIO.setup(RI2, GPIO.OUT)
    GPIO.setup(RE1, GPIO.OUT)

def loop():

    GPIO.output(FI1, GPIO.HIGH)
    GPIO.output(FI2, GPIO.LOW)
    GPIO.output(FE1, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(FI1, GPIO.LOW)
    GPIO.output(FI2, GPIO.HIGH)
    GPIO.output(FE1, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(FE1, GPIO.LOW)
    sleep(0.5)
    GPIO.output(AI1, GPIO.HIGH)
    GPIO.output(AI2, GPIO.LOW)
    GPIO.output(AE1, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(AI1, GPIO.LOW)
    GPIO.output(AI2, GPIO.HIGH)
    GPIO.output(AE1, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(AE1, GPIO.LOW)
    sleep(0.5)
    GPIO.output(EI1, GPIO.HIGH)
    GPIO.output(EI2, GPIO.LOW)
    GPIO.output(EE1, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(EI1, GPIO.LOW)
    GPIO.output(EI2, GPIO.HIGH)
    GPIO.output(EE1, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(EE1, GPIO.LOW)
    sleep(0.5)
    GPIO.output(RI1, GPIO.HIGH)
    GPIO.output(RI2, GPIO.LOW)
    GPIO.output(RE1, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(RI1, GPIO.LOW)
    GPIO.output(RI2, GPIO.HIGH)
    GPIO.output(RE1, GPIO.HIGH)
    sleep(0.3)
    GPIO.output(RE1, GPIO.LOW)
    sleep(0.5)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()