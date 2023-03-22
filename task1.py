import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.IN)

"""
a =  int(input())
for i in range(0,a,1):
    GPIO.output(22,1)
    time.sleep(1)
    GPIO.output(22,0)
    time.sleep(1)
    GPIO.output(22,1)

"""


GPIO.output(22,not(GPIO.input(23)))

