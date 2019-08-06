##
##
##

from ctx import Ctx
import zmq.green as zmq
import gevent
from gevent import monkey; monkey.patch_all()
from keyring import KeyRing

class Element:
    def __init__(self, name, ctx):
        self.ctx = ctx
        self.name = name
        self.namespace = ctx.namespace
        self.keys = KeyRing(namespace, name)
