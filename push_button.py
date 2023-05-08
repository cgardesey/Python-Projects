import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.output(10, True)

while True:
    if GPIO.input(10) == True:
        GPIO.output(8, False)
        time.sleep(0.5)
        GPIO.output(8, True)
        time.sleep(0.5)

    
        
    
    
