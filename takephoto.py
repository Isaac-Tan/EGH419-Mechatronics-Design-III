from picamera import PiCamera
from time import sleep
# import gpiozero
# import RPi.GPIO as GPIO
import wiringpi2 as wiringpi

# initialize
wiringpi.wiringPiSetup()

GPIO24 = 5
LOW = 0
INPUT = 0
PULL_DOWN = 1
wiringpi.pinMode(GPIO24, INPUT)  # push button
wiringpi.pullUpDnControl(GPIO24, PULL_DOWN)  # pull down


camera = PiCamera()

try:
    clear_all()
    while 1:
        button_state = wiringpi.digitalRead(GPIO24)
        print button_state
        if button_state == 1:
            camera.start_preview()
            sleep(5)
            camera.capture('/home/pi/Desktop/image1.jpg')
            camera.stop_preview()
        wiringpi.delay(20)
except KeyboardInterrupt:
    clear_all()

print("done")