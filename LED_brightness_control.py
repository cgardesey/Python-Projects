import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)
pwm.start(0)

while True:  
    for i in range(20, 0, -1):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)
    for i in range(20):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)
