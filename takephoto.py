from picamera import PiCamera
import time
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
	ts = timestamp()
	filename = str(ts)
	camera.capture('/home/pi/Photos/Testing/' + filename + extension)
	print "Image taken."
now = time.time()
takephoto()
elapsed = time.time() - now
print("Process: Take Photo")
print("Latency: ", elapsed)