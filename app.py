'''
	Raspberry Pi GPIO Status and Control
'''

import RPi.GPIO as GPIO
import integration as it
from flask import Flask, render_template, url_for, request, jsonify

# from picamera import PiCamera
# from flask_api import FlaskAPI

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

# ledPIN = 16
doorPIN = 25

doorSts = 0

it.setup()

GPIO.setup(doorPIN, GPIO.IN)
	
@app.route("/")
def index():
	return render_template('login.html')

@app.route("/<url>")
def webpage(url):
	if url == "home.html":
		return render_template('home.html')
	elif url == "checkin.html":
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


@app.route("/session", methods=['POST'])
def action():
	doorSts = request.form['id']
	templateData = {
		'doorStatus' : doorSts,
	}
	# print(request.form['id'])
	check=request.form["id"]
	if (check=="End Session"):
		it.startsession()
		print("start session")
	elif (check=="Start Session"):
		print("im about to end")
		it.endsession()
		templateData = {
		'doorStatus' : doorSts,
		}
		print("im about to take a photo")
		it.takeendphoto()
	return render_template('checkin.html',**templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=False)