##
##
##
import os
from BundData import bund2python

class BundCtx:
    def __init__(self, name='__root__', parent=None):
        self.name = name
        self.parent = parent
        self.ctx = {}
        self.data = {}
        self.var  = {}
        self.env  = {}
        self.codeblocks = {}
        if self.name == '__root__':
            for k in os.environ:
                self.data[k] = os.environ[k]
    def createContext(self, name, parent):
        self.ctx[name] = BundCtx(name, parent)
        return self.ctx[name]
    def registerData(self, name, val):
        self.data[name] = bund2python(val)
    def registerVar(self, name, val):
        self.var[name] = bund2python(val)
    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            if self.parent:
                return self.parent[key]
            else:
                return None
