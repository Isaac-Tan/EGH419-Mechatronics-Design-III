from picamera import PiCamera
from time import sleep
import gpiozero
import RPi.GPIO as GPIO
from dateutil.parser import parse as dp


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)#Button to GPIO23

import datetime

def timestamp():
	t = datetime.datetime.now()
	t_iso = t.isoformat()
	t_parsed = dp(t_iso)
	t_secs = t_parsed.strftime('%s')
	print (t_secs)
	return t_secs


camera = PiCamera()

try:
    while True:
    	button_state = GPIO.input(23)
    	if button_state == True:
    		print "Closed!"
    		camera.start_preview()
    		sleep(5)
    		filename = timestamp()
    		camera.capture('/home/pi/Photos/%s.jpg' filename)
    		camera.stop_preview()
    		time.sleep(0.2)
    	else:
    		print "Open!"
except:
	GPIO.cleanup()
