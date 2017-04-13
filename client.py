import socket
import RPi.GPIO as GPIO
import time

SENSOR = 4
HOST = '192.168.10.134'
PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN)

try:
  while True:
    if GPIO.input(SENSOR) == 1:
      s.send('sound detected!')
      data = s.recv(1024)
      print data
      time.sleep(1)
except KeyboardInterrupt:
  s.close()
  pass

GPIO.cleanup()
