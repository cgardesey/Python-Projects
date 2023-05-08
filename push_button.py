import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)
GPIO.output(8, False)

GPIO.setup(10, GPIO.IN)


while True:
    if GPIO.input(10) == True:
        GPIO.output(8, False)
    else:
	GPIO.output(8, True)


    
        
    
    
