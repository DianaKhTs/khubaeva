import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)

dac = [26,19,13,6,5,11,9,10]
GPIO.setup(dac,GPIO.OUT)
GPIO.output(dac,0)

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


try :
    while 1:
        print("Input a number from 0 to 255")
        res = input()
        if res == "q":
            print("NOT CORRECT!")
            break             
        try:
            n = int(res)
        except ValueError:
            print("not a digit number")
        else:
            if n > 255:
                print("more than 255")
            elif n < 0:
                print("error: negative input")
            else:
                GPIO.output(dac, decimal2binary(n))
                print("Power(V):", n / 256 * 3.3)
                time.sleep(2)
              
                
    
#except Exception: 
   # print('ERROR')78

finally: 
    GPIO.output(dac,0)
    GPIO.cleanup()