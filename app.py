# '''
# 	Raspberry Pi GPIO Status and Control
# '''

# import RPi.GPIO as GPIO
# from flask import Flask, render_template, url_for, request

# # from picamera import PiCamera
# # from flask_api import FlaskAPI

# app = Flask(__name__)
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# #define sensors GPIOs
# button = 23
# # senPIR = 16
# #define actuators GPIOs
# ledPIN = 16
# doorPIN = 24
# #Camera setup
# # camera = PiCamera()

# #initialize GPIO status variables
# # buttonSts = 0
# # senPIRSts = 0
# sessionSts=0
# lightSts=0
# doorSts = 0


# # Define button and PIR sensor pins as an input
# GPIO.setup(button, GPIO.IN)   
# # GPIO.setup(senPIR, GPIO.IN)
# # Define led pins as output
# GPIO.setup(ledPIN, GPIO.OUT)   
# GPIO.setup(doorPIN, GPIO.OUT)
# # GPIO.setup(ledYlw, GPIO.OUT) 
# # GPIO.setup(ledGrn, GPIO.OUT) 
# # turn leds OFF 
# GPIO.output(ledPIN, GPIO.LOW)
# GPIO.output(doorPIN, GPIO.LOW)
# # GPIO.output(ledGrn, GPIO.LOW)
	
# @app.route("/")
# def index():
# 	# Read GPIO Status
# 	sessionSts = GPIO.input(button)
# 	# senPIRSts = GPIO.input(senPIR)
# 	lightSts = GPIO.input(ledPIN)
# 	doorSts = GPIO.input(doorPIN)
# 	# ledGrnSts = GPIO.input(ledGrn)
# 	templateData = {
#       		'sessionStatus'  : sessionSts,
# 			# 'doorStatus' : doorSts,
#       		'lightStatus'  : lightSts,
# 			'switch1' : doorSts,
#       		'switch2'  : lightSts,
#       		# 'switch2'  : ledGrnSts,
#       	}
# 	return render_template('login.html', **templateData)

# @app.route("/<url>")
# def webpage(url):
# 	if url == "home.html":
# 		return render_template('home.html')
# 	elif url == "checkin.html":
# 		return render_template('checkin.html')
# 	elif url == "login.html":
# 		return render_template('login.html')
# 	elif url == "selectionpage.html":
# 		return render_template('selectionpage.html')
# 	elif url == "qrcodescanner.html":
# 		return render_template('qrcodescanner.html')
# 	elif url == "about.html":
# 		return render_template('about.html')
# 	return render_template('home.html')

	
# @app.route("/<deviceName>/<action>")
# def action(deviceName, action):
# 	if deviceName == 'session':
# 		if action == "on":

# 	if deviceName == 'light':
# 		actuator = ledPIN
# 		if action == "on":
# 			GPIO.output(actuator, GPIO.HIGH)
# 		if action == "off":
# 			GPIO.output(actuator, GPIO.LOW)
# 	if deviceName == 'door':
# 		actuator = doorPIN
# 		if action == 'on':
# 			GPIO.output(actuator, GPIO.HIGH)
# 			# GPIO.output(actuator, GPIO.LOW)
# 		if action == 'off':
# 			GPIO.output(actuator, GPIO.LOW)
# 	if deviceName == 'picture':
# 		if action == "on":
# 			# camera.capture('image/example1.png')
# 			GPIO.output(actuator, GPIO.LOW)
# 	sessionSts = GPIO.input(button)
# 	# senPIRSts = GPIO.input(senPIR)
# 	# ledRedSts = GPIO.input(ledRed)
# 	# ledYlwSts = GPIO.input(ledYlw)
# 	doorSts = GPIO.input(doorPIN)
# 	lightSts = GPIO.input(ledPIN)
   
# 	templateData = {
# 		'sessionStatus'  : sessionSts,
# 		'lightStatus'  : lightSts,
# 		'switch1' : doorSts,
# 		'switch2'  : lightSts,
# 		# 'switch2'  : ledGrnSts,
# 	}
# 	return render_template('checkin.html', **templateData)
# if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=80, debug=True)




'''
	Raspberry Pi GPIO Status and Control
'''

import RPi.GPIO as GPIO
import integration as it
from flask import Flask, render_template, url_for, request

# from picamera import PiCamera
# from flask_api import FlaskAPI

app = Flask(__name__)
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
#define sensors GPIOs
# button = 23
# senPIR = 16
#define actuators GPIOs

# ledPIN = 16
doorPIN = 25

#Camera setup
# camera = PiCamera()

#initialize GPIO status variables
# buttonSts = 0
# senPIRSts = 0

# sessionSts=0
# lightSts=0
doorSts = 0


# Define button and PIR sensor pins as an input
# GPIO.setup(button, GPIO.IN)   
# GPIO.setup(senPIR, GPIO.IN)
# Define led pins as output
# GPIO.setup(ledPIN, GPIO.OUT)   
GPIO.setup(doorPIN, GPIO.IN)
# GPIO.setup(ledYlw, GPIO.OUT) 
# GPIO.setup(ledGrn, GPIO.OUT) 
# turn leds OFF 
# GPIO.output(ledPIN, GPIO.LOW)
# GPIO.output(doorPIN, GPIO.LOW)
# GPIO.output(ledGrn, GPIO.LOW)
	
@app.route("/")
def index():
	# # Read GPIO Status
	# sessionSts = GPIO.input(button)
	# # senPIRSts = GPIO.input(senPIR)
	# lightSts = GPIO.input(ledPIN)
	# doorSts = GPIO.input(doorPIN)
	# # ledGrnSts = GPIO.input(ledGrn)
	# templateData = {
    #   		'sessionStatus'  : sessionSts,
	# 		# 'doorStatus' : doorSts,
    #   		'lightStatus'  : lightSts,
	# 		'switch1' : doorSts,
    #   		'switch2'  : lightSts,
    #   		# 'switch2'  : ledGrnSts,
    #   	}
	return render_template('login.html')

@app.route("/<url>")
def webpage(url):
	if url == "home.html":
		return render_template('home.html')
	elif url == "checkin.html":
		doorSts = GPIO.input(doorPIN)
		templateData = {
			'doorStatus' : doorSts,
      	}
		return render_template('checkin.html', **templateData)
	elif url == "login.html":
		return render_template('login.html')
	elif url == "selectionpage.html":
		return render_template('selectionpage.html')
	elif url == "qrcodescanner.html":
		return render_template('qrcodescanner.html')
	elif url == "about.html":
		return render_template('about.html')
	return render_template('home.html')


@app.route("/checkin.html/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'session':
		# actuator = doorPIN
		if action == 'on':
			it.unlock()
			# GPIO.output(actuator, GPIO.HIGH)
		# if action == 'off':
		# 	GPIO.output(actuator, GPIO.LOW)
	
			
	# if deviceName == 'light':
	# 	actuator = ledPIN
	# 	if action == "on":
	# 		GPIO.output(actuator, GPIO.HIGH)
	# 	if action == "off":
	# 		GPIO.output(actuator, GPIO.LOW)

	# if deviceName == 'door':
	# 	actuator = doorPIN
	# 	if action == 'on':
	# 		GPIO.output(actuator, GPIO.HIGH)
	# 		# GPIO.output(actuator, GPIO.LOW)
	# 	if action == 'off':
	# 		GPIO.output(actuator, GPIO.LOW)
	# if deviceName == 'picture':
	# 	if action == "on":
	# 		# camera.capture('image/example1.png')
	# 		GPIO.output(actuator, GPIO.LOW)


	# sessionSts = GPIO.input(button)
	# senPIRSts = GPIO.input(senPIR)
	# ledRedSts = GPIO.input(ledRed)
	# ledYlwSts = GPIO.input(ledYlw)
	doorSts = GPIO.input(doorPIN)
	# lightSts = GPIO.input(ledPIN)
   
	templateData = {
		# 'sessionStatus'  : sessionSts,
		# 'lightStatus'  : lightSts,
		'doorSts' : doorSts,
		# 'switch2'  : lightSts,
		# 'switch2'  : ledGrnSts,
	}
	return render_template('checkin.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=False)