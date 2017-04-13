import os
import socket
import redis_middle_class

HOST =  '192.168.10.134'
PORT = 5001

dbconn = redis_middle_class.Conn_db()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

message = dbconn.get('sensor')
print 'Current process pid:{0}, value of sensor:{1}'.format(os.getpid(), message)

print 'Server start at: %s:%s' %(HOST,PORT)
print 'wait for connection...'

try:
  while True:
    conn, addr = s.accept()
    print 'Connected by ',addr
    while True:
      data = conn.recv(1024)
      queue = dbconn.get('sensor')
      queue.append(data)
      dbconn.set('sensor', queue)
      conn.send('Server received the message')
except KeyboardInterrupt:
  s.close()
  pass
