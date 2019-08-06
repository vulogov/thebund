##
##
##
import uuid
import time
from queue import Queue
from collections import UserDict
from keyring import KeyRing

class Ctx(UserDict):
    def __init__(self, **args):
        UserDict.__init__(self)
        self.data = args
        self['consul'] = 'http://127.0.0.1:8500'
        self['vault'] = 'http://127.0.0.1:8200'
        self['namespace'] = 'bund'
        self['name'] = str(uuid.uuid4())
        self['id'] = str(uuid.uuid4())
        self['stamp'] = timre.time()
        self['q'] = {}
        self['q']['__main__'] = Queue()
        self['globals'] = {}
        self.keys = KeyRing()
    def push(self, data, q='__main__'):
        return self['q'][q].put_nowait(data)
    def pull(self, data, q='__main__'):
        return self['q'][q].get_nowait(data)
    def set(self, k, v):
        self['globals'][k] = v
    def get(self, k):
        self['globals'][k]
