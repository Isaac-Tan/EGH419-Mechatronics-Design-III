from picamera import PiCamera
from time import sleep
import gpiozero
import RPi.GPIO as GPIO
from dateutil.parser import parse as dp


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)#Button1 to GPIO23
GPIO.setup(16, GPIO.OUT)#LED to GPIO16
GPIO.setup(25, GPIO.IN)#Button2 to GPIO25


import datetime
sessionActive = False
camera = PiCamera()
GPIO.output(16,1)

def timestamp():
	t = datetime.datetime.now()
	t_iso = t.isoformat()
	t_parsed = dp(t_iso)
	t_secs = t_parsed.strftime('%s')
	return t_secs

# def end():
# 	sessiontime = starttime - endtime

def startsession():
	print "Starting Session!"
	sessionActive = True
	sleep(1)
	starttime = timestamp()
	filename = str(starttime)
	extension = ".jpg"
	camera.capture('/home/pi/Photos/Before/' + filename + extension)
	print "Image taken."
	GPIO.output(16, 0)
	sleep(5)

def endsession():
	print "Ending Session!"
	sleep(1)
	print "Please return the equipment to the locker and close the door."
	endtime = timestamp()
	filename = str(endtime)
	extension = ".jpg"
	camera.capture('/home/pi/Photos/After/' + filename + extension)
	print "Image taken."
	sessionActive = False
	GPIO.output(16, 1)
	sleep(5)



while True:
	button1_state = GPIO.input(23)
	if button1_state == True and sessionActive == False:
		startsession()
	else:
		print "-"
	button2_state = GPIO.input(25)
	if button2_state == True:
		endsession()
	else:
		print "--"