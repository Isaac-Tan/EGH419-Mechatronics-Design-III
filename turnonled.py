from time import sleep
import gpiozero
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setwarnings(False)

while True:
	GPIO.output(16,GPIO.HIGH)
	sleep(2)
	GPIO.output(16,GPIO.LOW)

GPIO.cleanup()