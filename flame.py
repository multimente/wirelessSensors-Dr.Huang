import RPi.GPIO as GPIO
import time

DOUT = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOUT, GPIO.IN)

try:
  while True:
    if GPIO.input(DOUT) == 1:
      print "Flame detected!"
      time.sleep(1)
except KeyboardInterrupt:
  pass

GPIO.cleanup()
