from picamera import PiCamera
from time import sleep
import gpiozero
import RPi.GPIO as GPIO
from dateutil.parser import parse as dp
import datetime

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.IN)				#LED switch to GPIO23
	GPIO.setup(24, GPIO.IN)				#Locked state switch to GPIO16
	GPIO.setup(25, GPIO.OUT)			#Solenoid lock to GPIO25
	GPIO.setup(16, GPIO.OUT)			#LED to GPIO16

setup()

sessionActive = False
camera = PiCamera()
GPIO.output(16,0)
opened = 0

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
	sleep(1.5)
	if (case == "start"):					#If the photo is taken at the start of a session
		starttime = timestamp()				#Sets the start time as the current unix timestamp
		filename = str(starttime)			#Names the photo as the timestamp
		camera.capture('/home/pi/Photos/Before/' + filename + extension)
	elif (case == "end"):					#If the photo is taken at the end of a session
		endtime = timestamp()				#Sets the end time as the current unix timestamp
		filename = str(endtime)				#Names the photo as the timestamp
		camera.capture('/home/pi/Photos/After/' + filename + extension)
	GPIO.output(16, 0)						#Sets the relay signal for the LED low


def unlock():
	print("unlocking")
	GPIO.setup(25, GPIO.OUT)
	GPIO.output(25, 1)					#Set relay signal pin high
	sleep(0.05)							#for 50ms
	GPIO.output(25, 0)					#Set relay signal pin low



def startsession():						#Starting a session
	takephoto("start")					#Take a photo of the interior
	unlock()							#Unlock the solenoid lock

def endsession():						#Ending a session
	unlock()							#Unlock the solenoid lock
	doorOpenstate = GPIO.input(24)		#Check if the door has been closed
	print(doorOpenstate)
	while doorOpenstate == 0:
		doorOpenstate = GPIO.input(24)		#Check if the door has been closed
		print("in loop")
		print(doorOpenstate)

def takeendphoto():
	takephoto("end")					#Take a photo of the interior




def led_callback(channel):
	if GPIO.input(23):					#If the door is opened
		GPIO.output(16, 1)				#Set the relay signal for the LED high
	else:								#If the door is closed
		GPIO.output(16,0)				#Set the relay signal for the LED low

# def door_callback(channel):
# 	if GPIO.input(24):
# 		opened = 0
# 	else:
# 		opened = 1

# def opened():
# 	if opened == 1:
# 		return 1
# 	else:
# 		return 0


GPIO.add_event_detect(23,GPIO.BOTH,callback=led_callback) # Setup event on pin 23 rising edge

# GPIO.add_event_detect(24,GPIO.BOTH,callback=door_callback) # Setup event on pin 23 rising edge

# takephoto("start")