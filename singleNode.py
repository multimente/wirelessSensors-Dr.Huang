import time
import thread
import json
from flask import Flask, request
import redis_middle_class

conn = redis_middle_class.Conn_db()

app = Flask(__name__)
#app.config['SECRET KEY'] = 'secret'
#socketio = SocketIO(app)

@app.route('/')
def home_page():
  #thread.start_new_thread(monitor, ('sensor-thread',))
  #return render_template('index.html')
  return 'Wireless Sensor network'

@app.route('/query', methods=['GET'])
def query():
  count = int(request.args.get('count',0))
  message_queue = conn.get('sensor')
  if len(message_queue) != 0:
    data = {'data': message_queue[count:],'count': len(message_queue)}
    return json.dumps(data)
  else:
    return json.dumps({'data':'','count':0})

'''
@socketio.on('connect')
def test_message():
  emit('my response', {'data': 'socketio connected'})
'''

if __name__ == 'main':
  #socketio.run(app)
  app.run(host='0.0.0.0')
