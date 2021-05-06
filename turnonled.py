from time import sleep
import gpiozero
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)#LED to GPIO24
GPIO.setwarnings(False)

while True:
	GPIO.output(24,1)
	sleep(2)
	GPIO.output(24,0)

GPIO.cleanup()