##
##
##
from BundData import bund2python

class BundCtx:
    def __init__(self, name='__root__', parent=None):
        self.name = name
        self.parent = parent
        self.ctx = {}
        self.data = {}
        self.var  = {}
        self.codeblocks = {}
    def createContext(self, name, parent):
        self.ctx[name] = BundCtx(name, parent)
        return self.ctx[name]
    def registerData(self, name, val):
        self.data[name] = bund2python(val)
