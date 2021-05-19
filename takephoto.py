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

def takephoto(cond):
	extension = ".jpg"
	if (cond == "pre"):
		starttime = timestamp()
		filename = str(starttime)
		camera.capture('/home/pi/Photos/Before/' + filename + extension)
	elif (cond == "post"):
		endtime = timestamp()
		filename = str(endtime)
		camera.capture('/home/pi/Photos/After/' + filename + extension)
	if (cond == "pre" or cond == "post"):
		print "Image taken."


# def end():
# 	sessiontime = starttime - endtime

def startsession():
	print "Starting Session!"
	sleep(1)
	takephoto("pre")
	sleep(5)

def endsession():
	print "Ending Session!"
	sleep(1)
	print "Please return the equipment to the locker and close the door."
	sleep(3)
	takephoto("post")
	sleep(5)



startsession()