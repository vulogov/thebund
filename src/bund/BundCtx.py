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
    def getFromRel(self, name, name_of_dat):
        try:
            d = getattr(self, name_of_dat)
        except AttributeError:
            return None
        if name in d:
            return d[name]
        else:
            if self.parent:
                return self.getFromRel(name, name_of_dat)
            else:
                return None
    def getEnv(self, name):
        return self.getFromRel(name, "env")
    def __getitem__(self, key):
        return self.getFromRel(key, "data")
