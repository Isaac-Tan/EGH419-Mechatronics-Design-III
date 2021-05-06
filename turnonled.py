from time import sleep
import gpiozero
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)#Button1 to GPIO23
GPIO.setup(24, GPIO.OUT)#LED to GPIO24
GPIO.setup(25, GPIO.IN)#Button2 to GPIO25

GPIO.output(24, 1)

GPIO.cleanup()