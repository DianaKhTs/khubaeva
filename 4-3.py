import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
p = GPIO.PWM(22, 100)
try:
    while(1):
        ch = int(input('print ch (1000Hz)'))#1000
        p = GPIO.PWM(22, ch)
        ds = int(input('print ds')) #%
        p.start(ds)
        print(ds * 3.3 / 100)
        
    
finally:
    GPIO.cleanup()