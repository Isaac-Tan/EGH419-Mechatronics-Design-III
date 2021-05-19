from picamera import PiCamera
from time import sleep
from dateutil.parser import parse as dp


import datetime
camera = PiCamera()

def timestamp():
	t = datetime.datetime.now()
	t_iso = t.isoformat()
	t_parsed = dp(t_iso)
	t_secs = t_parsed.strftime('%s')
	return t_secs

def takephoto():
	extension = ".jpg"
	filename = str(timestamp())
	camera.capture('/home/pi/Photos/Testing/' + filename + extension)
	print "Image taken."

takephoto()