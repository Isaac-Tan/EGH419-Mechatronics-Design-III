import time
from time import sleep
import gpiozero
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)#LED to GPIO24


while True:
	now = time.time()	#start process time
	GPIO.output(25, 1)
	sleep(0.05)
	GPIO.output(25, 0)
	sleep(5)
	elapsed = time.time() - now			#end process time
	print("Process: Open Door")
	print("Latency: ", elapsed)


GPIO.cleanup()