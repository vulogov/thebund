##
## bund message interface
##

import time
import uuid
import msgpack
import socket
import rsa
from collections import UserDict


class Message(UserDict):
    def __init__(self, **data):
        UserDict.__init__(self)
        if '_data' in data:
            self.load(data['_data'])
        if '_keys' in data:
            self.keys = data['_keys']
        else:
            self.keys = None
        self.data = {}
        self.data['stamp']   = time.time()
        self.data['seal']    = False
        self.data['version'] = 1.0
        self.data['from']    = None
        self.data['to']      = ['*']
        self.data['id']      = '%s@%s'%(socket.gethostname(), str(uuid.uuid4()))
        self.data['type']    = 'generic/message'
        self.data['msg']     = None
        for key in data:
            if key[0] == '_':
                continue
            self.data[key] = data[key]
    def dumps(self):
        return msgpack.packb(self.data, use_bin_type=True)
    def load(self, data):
        self.data = msgpack.unpackb(data)
    def seal(self, key=None):
        if not key:
            key = self.keys.keys.key
        data = self.dumps()
        sign = rsa.sign(data, key, 'SHA-512')
        return msgpack.packb({'seal': True,
                                'msg': data,
                                'sign': sign,
                                'name': self.keys.name})
    def unseal(self, data):
        if not self.keys:
            return False
        _data = msgpack.unpackb(data)
        if not _data[b'seal']:
            return False
        try:
            rsa.verify(_data[b'msg'], _data[b'sign'], self.keys[_data[b'name'].decode('utf-8')])
            self.load(_data[b'msg'])
            return True
        except:
            return False




if __name__ == '__main__':
    import keyring
    kr = keyring.KeyRing()
    m = Message(msg="Hello world!", _keys=kr)
    d = m.dumps()
    print("A sample message", repr(d))
    m2 = Message(_data=d, _keys=kr)
    print("A message ID",m['id'])
    e = m2.seal()
    print("Sealed message",repr(e))
    print("Seal verification", m2.unseal(e))
