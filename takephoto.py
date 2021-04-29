from picamera import PiCamera
from time import sleep
import gpiozero
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)#Button to GPIO23


camera = PiCamera()

try:
    while True:
    	button_state = GPIO.input(23)
    	if button_state == True:
    		print "Open!"
    		# camera.start_preview()
    		# sleep(5)
    		# camera.capture('/home/pi/Desktop/image1.jpg')
    		# camera.stop_preview()
    		# time.sleep(0.2)
    	else:
    		print "Closed!"
except:
	GPIO.cleanup()
