import redis
import pickle

class Conn_db():
  def __init__(self):
      self.conn = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0)

  def set(self, key_, value_):
      value_ = pickle.dumps(value_)
      self.conn.set(key_, value_)

  def get(self, key_):
      value_ = self.conn.get(key_)
      if value_ != None:
          value_ = pickle.loads(value_)
          return value_
      else:
          return []
