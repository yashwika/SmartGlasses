import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TRIG = 18
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)

class Distance:
    def get_distance():
           GPIO.output(TRIG, True)
           time.sleep(0.00001)
           GPIO.output(TRIG, False)
    
           while GPIO.input(ECHO)==0:
              pulse_start = time.time()
    
           while GPIO.input(ECHO)==1:
              pulse_end = time.time()
    
           pulse_duration = pulse_end - pulse_start
    
           distance = pulse_duration * 17150
    
           #distance = round(distance+1.15, 2)
           return distance