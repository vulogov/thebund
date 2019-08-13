##
##
##
import os
import sys
from BundData import bund2python
from BundGrammarChannel import createStandardChannels, createInChannel, createOutChannel

class BundCtx:
    def __init__(self, name='__root__', parent=None):
        self.name = name
        self.parent = parent
        self.ctx = {}
        self.data = {}
        self.var  = {}
        self.env  = {}
        self._in = {}
        self._out = {}
        self.codeblocks = {}
        if self.name == '__root__':
            for k in os.environ:
                self.data[k] = os.environ[k]
            createStandardChannels(self)
    def createContext(self, name, parent):
        if name not in self.ctx:
            self.ctx[name] = BundCtx(name, parent)
        return self.ctx[name]
    def registerData(self, name, val):
        self.data[name] = bund2python(val)
        print(self.data[name])
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
    def getInChannel(self, name):
        return self.getFromRel(name, "_in")
    def getOutChannel(self, name):
        return self.getFromRel(name, "_out")
    def registerInChannel(self, btype, name,  attr, ch_type, ch_name):
        createInChannel(self, btype, name,  attr, ch_type, ch_name)
    def registerOutChannel(self, btype, name,  attr, ch_type, ch_name):
        createOutChannel(self, btype, name,  attr, ch_type, ch_name)
    def __call__(self, name):
        if name in self.ctx:
            return self.ctx[name]
        else:
            for n in self.ctx[n]:
                return self.ctx[n].__call__(name)
        return None
