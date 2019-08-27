##
##
##
from BundData import bund2python
from BundData import CODEBLOCKREF,CODEBLOCK,CODEWORDLAZY,CODEWORDLAZYEVAL,CODEWORDLATEBIND

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
            t, code, arity = self.CB(mod, name)
        else:
            t, code, arity = C(name)
        if t not in [1]:
            return False
        res = self._e(arity, code)
        while True:
            res = self.pull()
            if not res:
                break
            print("*",res)
    def _e(self, arity, c):

        if len(c) == 0:
            self.error("There is nothing to do for me here")
            return None
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
        elif isinstance(self._current, tuple):
            if len(self._current) == 2:
                _code_type, _c = self._current
            else:
                self.error("Unknown arity in {}", self._current)
                return None
            if _code_type == CODEBLOCK:
                self._e(_c)
            elif _code_type == CODEWORDLATEBIND:
                module, n = _c
                d = self.ctx.VAR(module, n)
                if not d:
                    d = self.ctx.DATA(module, n)
                    if not d:
                        self.log.error("{}->{} can not be late-binded as it unknown.", module, n)
                self.push(bund2python(self.ctx, d))
            elif _code_type == CODEBLOCKREF:
                self.push((_code_type, _c))
            elif _code_type == CODEWORDLAZY:
                self.push((_code_type, _c))
            elif _code_type == CODEWORDLAZYEVAL:
                self.lazy()
        else:
            self.log.debug("%s detected"%self._current)
        return self._e(arity, c[1:])
    def mkWord(self, w):
        res = ""
        if w.prefix:
            res+=w.prefix
        if w.word:
            res+=w.word
        if w.suffix:
            res+=w.suffix
        return res
    def lazy(self):
        _p = []
        w = None
        while True:
            d = self.pull()
            if d == None:
                self.log.error("Requested a lazy evaluation, but stack is exausted")
                break
            if isinstance(d, tuple) and d[0] == CODEWORDLAZY:
                w = d[1]
                break
            else:
                _p.append(d)
        _p.reverse()
        _p = tuple(_p)
        if w:
            if w.__class__.__name__ == 'CodeWordNoParam':
                w = self.mkWord(w)
            self.log.debug("Lazy {} ({})", w, _p)
