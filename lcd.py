from RPLCD import *
import RPi.GPIO as GPIO
import os, time

lcd = CharLCD(cols=16, rows=2, pin_rs=3, pin_e=5, pins_data=[29, 31, 33, 35])

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)

GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

GPIO.setup(37, GPIO.IN, pull_up_down = GPIO.PUD_UP)

fire_room_1 = False
fire_room_2 = False
fire_room_3 = False

with cursor(lcd, 0, 0):
    lcd.write_string(u'  1    2    3  ')

while True:
    if GPIO.input(11) == True:
        GPIO.output(19, False)
        fire_room_1 = False
	with cursor(lcd, 1, 0):
                lcd.write_string(u'    ')         	     
    else:
        GPIO.output(19, True)
        fire_room_1 = True
	with cursor(lcd, 1, 0):
                lcd.write_string(u'Fire')

    if GPIO.input(13) == True:
        GPIO.output(21, False)
        fire_room_2 = False
	with cursor(lcd, 1, 5):
                lcd.write_string(u'    ')         	     
    else:
        GPIO.output(21, True)
        fire_room_2 = True
	with cursor(lcd, 1, 5):
                lcd.write_string(u'Fire')

    if GPIO.input(15) == True:
        GPIO.output(23, False)
        fire_room_3 = False
	with cursor(lcd, 1, 10):
                lcd.write_string(u'    ')         	     
    else:
        GPIO.output(23, True)
        fire_room_3 = True
	with cursor(lcd, 1, 10):
                lcd.write_string(u'Fire')



    if fire_room_1 == True or fire_room_2 == True or fire_room_3 == True:
        GPIO.output(40, True)
    else:
        GPIO.output(40, False)

        

    if GPIO.input(37) == False:
        GPIO.output(40, False)
        GPIO.output(19, False)
        GPIO.output(21, False)
        GPIO.output(23, False)
        lcd.clear()
        with cursor(lcd, 0, 0):
                lcd.write_string(u'  Shutting')
        with cursor(lcd, 1, 0):
                lcd.write_string(u'      down')
        for i in range(3):
            with cursor(lcd, 1, i + 10):
                lcd.write_string(u'.')
                time.sleep(1)
        lcd.clear()
        os.system("shutdown -h now")
        
             

           
