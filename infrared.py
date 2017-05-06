import RPi.GPIO as GPIO
import time

DOUT = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOUT, GPIO.IN)

try:
  while True:
    if GPIO.input(DOUT) == 0:
      print 'Obstacle detected!'
      time.sleep(1)
    else:
	  print 'nothing'
except KeyboardInterrupt:
  pass

GPIO.cleanup()
