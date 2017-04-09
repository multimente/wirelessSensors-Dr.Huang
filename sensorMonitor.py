import RPi.GPIO as GPIO
import time

SENSOR = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN)

def monitor(threadName):
  print threadName + 'is running'
  try:
    while True:
      if GPIO.input(SENSOR) == 1:
        print 'detect sound'
        time.sleep(1)
  except KeyboardInterrupt:
    pass
    GPIO.cleanup()
