from picamera import PiCamera
from time import sleep
import gpiozero
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23


camera = PiCamera()

try:
    while True:
    	button_state = GPIO.input(23)
    	if button_state == False:
    		GPIO.output(24, True)
    		camera.start_preview()
    		sleep(5)
    		camera.capture('/home/pi/Desktop/image1.jpg')
    		camera.stop_preview()
    		time.sleep(0.2)
except:
	GPIO.cleanup()
