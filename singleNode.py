import time
import RPi.GPIO as GPIO
from flask import Flask, render_template

SENSOR = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN)

app = Flask(__name__)

@app.route('/')
def home_page():
  return 'Hello World!'

if __name__ == 'main':
  app.run()
