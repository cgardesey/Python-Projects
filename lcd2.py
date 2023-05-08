from RPLCD import *
import RPi.GPIO as GPIO
import time

lcd = CharLCD(cols=16, rows=2, pin_rs=3, pin_e=5, pins_data=[29, 31, 33, 35])

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(12, GPIO.IN)


with cursor(lcd, 0, 0):
    lcd.write_string(u'  1    2    3  ')

while True:
    if GPIO.input(8) == True:
	with cursor(lcd, 1, 0):
                lcd.write_string(u'    ')         	     
    else:
	with cursor(lcd, 1, 5):
                lcd.write_string(u'Fire')

    if GPIO.input(10) == True:
	with cursor(lcd, 1, 5):
                lcd.write_string(u'    ')         	     
    else:
	with cursor(lcd, 1, 0):
                lcd.write_string(u'Fire')

    if GPIO.input(12) == True:
	with cursor(lcd, 1, 10):
                lcd.write_string(u'    ')         	     
    else:
	with cursor(lcd, 1, 10):
                lcd.write_string(u'Fire') 
             

           
