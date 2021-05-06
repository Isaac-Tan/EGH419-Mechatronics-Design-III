from picamera import PiCamera
from time import sleep
import gpiozero
import RPi.GPIO as GPIO
from dateutil.parser import parse as dp


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)#Button1 to GPIO23
GPIO.setup(24, GPIO.OUT)#LED to GPIO24
GPIO.setup(25, GPIO.IN)#Button2 to GPIO25


import datetime

def timestamp():
	t = datetime.datetime.now()
	t_iso = t.isoformat()
	t_parsed = dp(t_iso)
	t_secs = t_parsed.strftime('%s')
	return t_secs


camera = PiCamera()
GPIO.output(24,1)


while True:
	button1_state = GPIO.input(23)
	if button1_state == True:
		print "Closed!"
		sleep(1)
		filename = str(timestamp())
		extension = ".jpg"
		camera.capture('/home/pi/Photos/before '+ filename + extension)
		GPIO.output(24, 0)
		sleep(5)
	else:
		print "Open!"
	button2_state = GPIO.input(25)
	if button2_state == True:
		print "Closed!"
		sleep(1)
		filename = str(timestamp())
		extension = ".jpg"
		camera.capture('/home/pi/Photos/after '+ filename + extension)
		GPIO.output(24, 1)
		sleep(5)
	else:
		print "Open!"