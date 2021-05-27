from time import sleep
import gpiozero
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)#LED to GPIO24

GPIO.output(25, 1)
sleep(0.25)
GPIO.output(25, 0)

GPIO.cleanup()