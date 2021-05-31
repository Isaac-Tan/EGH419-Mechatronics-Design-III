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

def timestamp():
	t = datetime.datetime.now()			#Obtains the current timestamp
	t_iso = t.isoformat()				#Converts to iso format
	t_parsed = dp(t_iso)
	t_unix = t_parsed.strftime('%s')	#Time in unix format
	return t_unix

def takephoto(case):
	GPIO.output(16, 1)						#Sets the relay signal for the LED high
	extension = ".jpg"						#Sets the image extension as .jpg
	camera.start_preview()
	sleep(2)
	if (case == "start"):					#If the photo is taken at the start of a session
		starttime = timestamp()				#Sets the start time as the current unix timestamp
		filename = str(starttime)			#Names the photo as the timestamp
		camera.capture('/home/pi/Photos/Before/' + filename + extension)
	elif (case == "end"):					#If the photo is taken at the end of a session
		endtime = timestamp()				#Sets the end time as the current unix timestamp
		filename = str(endtime)				#Names the photo as the timestamp
		camera.capture('/home/pi/Photos/After/' + filename + extension)
	sleep(1)								#Allows camera to take photo
	GPIO.output(16, 0)						#Sets the relay signal for the LED low


	# if (case == "pre" or case == "post"):	#Once successfully taking a photo
	# 	print "Image taken."				#Print feedback

def unlock():
	GPIO.output(25, 1)					#Set relay signal pin high
	sleep(0.05)							#for 50ms
	GPIO.output(25, 0)					#Set relay signal pin low


# def end():
# 	sessiontime = starttime - endtime

def startsession():				#Starting a session
	sessionActive = True		#Set the session as active so it cannot be started again but can be ended
	takephoto("start")			#Take a photo of the interior
	unlock()					#Unlock the solenoid lock

def endsession():						#Ending a session
	unlock()							#Unlock the solenoid lock
	sleep(3)
	# checkclosed()						#Check if the door has been closed
	doorOpenstate = GPIO.input(24)
	while doorOpenstate == True:
		print("close the door")
	sessionActive = False				#Set the session as inactive so it cannot be ended again but can be started
	sessionTime = endtime - starttime
	takephoto("end")					#Take a photo of the interior


# takephoto("start")
# while sessionActive:
# 	ledSwitch_state = GPIO.input(23)
# 	if ledSwitch_state == True:			#If the door is opened
# 		GPIO.output(16, 1)				#Set the relay signal for the LED high
# 	else:								#If the door is closed
# 		GPIO.output(16,0)				#Set the relay signal for the LED low


