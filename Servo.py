import RPi.GPIO as GPIO
import time

l = 0
r = 0

lservopin = 11
rservopin = 13

GPIO.setmode(GPIO.board)

GPIO.setup(lservopin, GPIO.OUT)
GPIO.setup(rservopin, GPIO.OUT)

lPWM = GPIO.PWM(lservopin, 50)
rPWM = GPIO.PWM(rservopin, 50)
lPWM.start(5)
rPWM.start(5)

while(l < 5):
    for i in range(45, 135):
        position = 1./18*(i)+2
        lPWM.ChangeDutyCycle(position)
        time.sleep(0.005)

    for i in range(135, 45, -1):
        position = 1./18*(i)+2
        lPWM.ChangeDutyCycle(position)
        time.sleep(0.005)
    l = l + 1
lPWM.stop()

while(r < 5):
    for i in range(135, 45, -1):
        position = 1./18*(i)+2
        rPWM.ChangeDutyCycle(position)
        time.sleep(0.005)

    for i in range(45, 135):
        position = 1./18*(i)+2
        rPWM.ChangeDutyCycle(position)
        time.sleep(0.005)
    r = r + 1

rPWM.stop()
GPIO.cleanup()