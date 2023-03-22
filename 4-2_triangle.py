import RPi.GPIO as GPIO
import time

dac = [26,19,13,6,5,11,9,10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac,GPIO.OUT)



def dec2bin(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try :

    T = int(input("print T: "))
    n = int(input('print num of tr: '))
    for k in range(n):
        for i in range(255):
            val = dec2bin(i)
            GPIO.output(dac, val)
            time.sleep(T/510)
            print("Power(V):", i/ 256 * 3.3)
        for i in range(255, 0, -1):
            val = dec2bin(i)
            GPIO.output(dac, val)
            time.sleep(T/510)
            print("Power(V):", i / 256 * 3.3)


finally: 
    GPIO.output(dac,0)
    GPIO.cleanup()