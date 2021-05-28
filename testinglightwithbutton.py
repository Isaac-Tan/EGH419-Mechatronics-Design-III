from time import sleep
import gpiozero
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)				#Button1 to GPIO23
GPIO.setup(16, GPIO.OUT)			#LED to GPIO16

while True:
	ledSwitch_state = GPIO.input(23)
	if ledSwitch_state == True:			#If the door is opened
		GPIO.output(16, 1)				#Set the relay signal for the LED high
	else:								#If the door is closed
		GPIO.output(16,0)				#Set the relay signal for the LED low