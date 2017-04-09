import time
import thread
from flask import Flask, render_template
from sensorMonitor import *

#SENSOR = 4
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(SENSOR, GPIO.IN)

app = Flask(__name__)

@app.route('/')
def home_page():
  thread.start_new_thread(monitor, ('sensor-thread',))
  return 'hello'

if __name__ == 'main':
  app.run()
