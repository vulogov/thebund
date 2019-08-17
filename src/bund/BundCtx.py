##
##
##
import os
import sys
from BundData import bund2python
from BundGrammarSys import parseArgv
from BundGrammarChannel import createStandardChannels, createInChannel, createOutChannel

class BundCtx:
    def __init__(self, name='__root__', parent=None, parser=None):
        self.name = name
        self.parser = parser
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
            self.data['argv'] = parseArgv()
            print("argv is {}", self.data['argv'])
    def createContext(self, name, parent):
        if name not in self.ctx:
            self.ctx[name] = BundCtx(name, parent, self.parser)
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
    def getFromUp(self, name, name_of_dat):
        try:
            d = getattr(self, name_of_dat)
        except AttributeError:
            return None
        if name in d:
            return d[name]
        else:
            for c in self.ctx:
                res = self.ctx[c].getFromUp(name, name_of_dat)
                if res:
                    return res
        return None
    def getEnv(self, name):
        return self.getFromRel(name, "env")
    def __getitem__(self, key):
        return self.getFromRel(key, "data")
    def getInChannel(self, name):
        return self.getFromRel(name, "_in")
    def getOutChannel(self, name):
        return self.getFromRel(name, "_out")
    def C(self, name):
        c = self.getFromRel(name, "codeblocks")
        if not c:
            root = self.getParent()
            c = root.getFromUp(name, "codeblocks")
        return c
    def CB(self, module, name):
        root = self.getParent()
        if module in root.ctx:
            if name in root.ctx[module].codeblocks:
                return root.ctx[module].codeblocks[name]
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
    def getParent(self):
        if self.parent == None:
            return self
        return self.parent.getParent()
    def registerCode(self, name, c):
        if name in self.codeblocks:
            self.parser.log.debug("%s already been registered. Overwrite!"%name)
        self.codeblocks[name] = bund2python(c)
        print(self.name, self.codeblocks)
