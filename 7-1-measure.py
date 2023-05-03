import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
measured_data=[]
dac = [26,19,13,6,5,11,9,10]
comp = 4

troyka = 17
GPIO.setup(dac,GPIO.OUT)
GPIO.output(dac,0)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


    
def adc():
    for value in range(256):
        GPIO.output(dac, decimal2binary(value))
        time.sleep(0.002)
        compValue = GPIO.input(comp)
        if compValue == 0:
            return value

st_tm = time.time() 
n=0
try:
    while True:
        n+=1
        end_tm = time.time()
        tm = end_tm - st_tm
        value = adc()
        print(value)
        measured_data.append(value)
        plt.plot(measured_data)
        md = [str(i) for i in measured_data]
        with open ("data.txt","w") as outfile:
                outfile.write("\n".join(md))
        if value >= 245:
            GPIO.output(troyka,0)

        if value <= 10 and tm > 15:
             plt.show()
             params = [tm,n/tm, 3.3/255]
             p = [str(i) for i in params]
             print(tm, n/tm, 3.3/255)
             with open ("settings.txt","w") as outfile:
                outfile.write("\n".join(p))
             break
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
