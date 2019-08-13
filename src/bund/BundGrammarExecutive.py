##
##
##

class BundGrammarExecutive:
    def __init__(self):
        self._current = None
        self._rest = None
    def C(self, name):
        code = self.ctx.C(name)
        return code
    def CB(self, mod, name):
        code = self.ctx.CB(mod, name)
        return code
    def EVAL(self, name):
        if "->" in name:
            mod, name = name.split("->")
            t, code = self.CB(mod, name)
        else:
            t, code = C(name)
        if t not in [1]:
            return False
        return self._e(code)
    def _e(self, c):
        if len(c) == 0:
            return
        self._current = c[:1]
        self._rest = c[1:]
        print(self._current)
        return self._e(c[1:])
