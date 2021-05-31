from picamera import PiCamera
import time
from time import sleep
from dateutil.parser import parse as dp
import gpiozero
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)#LED to GPIO24



import datetime
camera = PiCamera()

def timestamp():
	t = datetime.datetime.now()
	t_iso = t.isoformat()
	t_parsed = dp(t_iso)
	t_secs = t_parsed.strftime('%s')
	return t_secs

def takephoto():
	GPIO.output(16, 1)						#Sets the relay signal for the LED high
	extension = ".jpg"
	ts = timestamp()
	filename = str(ts)
	camera.capture('/home/pi/Photos/Testing/' + filename + extension)
	camera.close()
	print "Image taken."
	GPIO.output(16, 0)						#Sets the relay signal for the LED low


now = time.time()
takephoto()
elapsed = time.time() - now
print("Process: Take Photo")
print("Latency: ", elapsed)
GPIO.cleanup()