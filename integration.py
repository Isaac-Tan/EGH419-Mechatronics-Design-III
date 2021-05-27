from picamera import PiCamera
from time import sleep
import gpiozero
import RPi.GPIO as GPIO
from dateutil.parser import parse as dp


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)				#Button1 to GPIO23
GPIO.setup(16, GPIO.OUT)			#LED to GPIO16
GPIO.setup(25, GPIO.IN)				#Button2 to GPIO25


import datetime
sessionActive = False
camera = PiCamera()
GPIO.output(16,0)

def timestamp():						#Obtains the current timestamp
	t = datetime.datetime.now()
	t_iso = t.isoformat()				#Converts to iso format
	t_parsed = dp(t_iso)
	t_secs = t_parsed.strftime('%s')	#Time in unix format
	return t_secs

def takephoto(case):
	extension = ".jpg"					#Sets the image extension as .jpg
	if (case == "pre"):					#If the photo is taken at the start of a session
		starttime = timestamp()			#Sets the start time as the current unix timestamp
		filename = str(starttime)		#Names the photo as the timestamp
		camera.capture('/home/pi/Photos/Before/' + filename + extension)
	elif (case == "post"):			#If the photo is taken at the end of a session
		endtime = timestamp()			#Sets the end time as the current unix timestamp
		filename = str(endtime)			#Names the photo as the timestamp
		camera.capture('/home/pi/Photos/After/' + filename + extension)
	if (case == "pre" or case == "post"):	#Once successfully taking a photo
		print "Image taken."				#Print feedback


# def end():
# 	sessiontime = starttime - endtime

def startsession():				#Starting a session
	print "Starting Session!"
	sessionActive = True		#Set the session as active so it cannot be started again but can be ended
	sleep(1)
	takephoto("pre")			#Take a photo of the interior
	GPIO.output(16, 0)			#Unlock the solenoid
	sleep(5)

def endsession():				#Ending a session
	print "Ending Session!"
	sessionActive = False		#Set the session as inactive so it cannot be ended again but can be started
	sleep(1)
	print "Please return the equipment to the locker and close the door."
	sleep(3)
	takephoto("post")			#Take a photo of the interior
	GPIO.output(16, 1)			#Lock the solenoid
	sleep(5)



while True:
	button1_state = GPIO.input(23)
	if button1_state == True:
		# startsession()
		GPIO.output(16, 1)
	else:
		GPIO.output(16,0)
		print ""
	# button2_state = GPIO.input(25)
	# if button2_state == True:
	# 	# endsession()
	# else:
	# 	print ""