import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

motor1A = 02
motor1B = 03
motor1E = 04

GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor1E, GPIO.OUT)

print("Motor going to start")

GPIO.output(motor1A, GPIO.HIGH)
GPIO.output(motor1B, GPIO.LOW)
GPIO.output(motor1E, GPIO.HIGH)
sleep(5)
print("Motor going to stop")
GPIO.output(motor1A, GPIO.LOW)
GPIO.cleanup()