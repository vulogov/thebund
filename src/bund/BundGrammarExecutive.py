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
        res = self._e(code)
        while True:
            res = self.pull()
            if not res:
                break
            print("*",res)
    def _e(self, c):
        if len(c) == 0:
            return
        self._current = c[0]
        self._rest = c[1:]
        self.log.debug("{} is here", self._current)
        if isinstance(self._current, int):
            self.push(self._current)
        elif isinstance(self._current, float):
            self.push(self._current)
        elif isinstance(self._current, bool):
            self.push(self._current)
        elif isinstance(self._current, list):
            self.push(self._current)
        elif isinstance(self._current, dict):
            self.push(self._current)
        else:
            self.log.debug("%s detected"%self._current)
        return self._e(c[1:])
