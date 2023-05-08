import serial
import RPi.GPIO as GPIO
import os, time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)

# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write('ATE0'+'\r\n')      # Disable the Echo
time.sleep(1)
port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
time.sleep(1)


def sendSMS(msg):

    port.write('AT+CMGF=1'+'\r\n')
    time.sleep(1)
    
    port.write('AT+CMGS="+233546676098"'+'\r\n')
    time.sleep(1)
 
    port.write(msg+'\r\n')  # Message
 
    port.write("\x1A") # Enable to send SMS
    time.sleep(3)
    return

while True:
    if GPIO.input(11) == False:
	sendSMS('Fire detected in room 1')
     

    if GPIO.input(13) == False:
	sendSMS('Fire detected in room 2')
        

    if GPIO.input(15) == True:
	sendSMS('Fire detected in room 3')



             

           
