import time
import RPi.GPIO as GPIO

DOUT = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOUT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

prevState = False
curState  = False

try:
  while True:
    time.sleep(0.5)
    prevState = curState
    curState = GPIO.input(DOUT)
    if curState != prevState:
      newState = "No Smoke Detected!" if curState else "Smoke Detected!"
      print "GPIO Pin %s is %s" % (DOUT, newState)
    time.sleep(1)
except KeyboardInterrupt:
  pass

GPIO.cleanup()
