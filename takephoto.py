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

def takephoto(case):
	extension = ".jpg"
	if (case == "pre"):
		starttime = timestamp()
		filename = str(starttime)
		camera.capture('/home/pi/Photos/Before/' + filename + extension)
	else if (case == "post"):
		endtime = timestamp()
		filename = str(endtime)
		camera.capture('/home/pi/Photos/After/' + filename + extension)
	if (case == "pre" or case == "post"):
		print "Image taken."


# def end():
# 	sessiontime = starttime - endtime

def startsession():
	print "Starting Session!"
	sessionActive = True
	sleep(1)
	takephoto("pre")
	GPIO.output(16, 0)
	sleep(5)

def endsession():
	print "Ending Session!"
	sessionActive = False
	sleep(1)
	print "Please return the equipment to the locker and close the door."
	sleep(3)
	takephoto("post")
	GPIO.output(16, 1)
	sleep(5)



while True:
	button1_state = GPIO.input(23)
	if button1_state == True:
		startsession()
	else:
		print ""
	button2_state = GPIO.input(25)
	if button2_state == True:
		endsession()
	else:
		print ""