import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)

dac = [26,19,13,6,5,11,9,10]
number = [0,0,0,0,0,0,0,0]
test = [255,127,64,32,5,0,256]
GPIO.setup(dac,GPIO.OUT)
def revert(num,number):
    for i in range(0,8):
        number[7-i] = num%2
        num=(num-num%2)//2


for i in range(0,7):
    revert(test[i],number)
    GPIO.output(dac,number)
    time.sleep(10)
    GPIO.output(dac,0)




GPIO.cleanup()