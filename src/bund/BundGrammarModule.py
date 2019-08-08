##
##
##

class BundGrammarModule:
    def registerModule(self, name, m):
        self.ctx.env[name] = m
    def loadPythonModule(self, name, param, r_name):
        import importlib
        if not r_name:
            r_name = name
        m = self.ctx.getEnv(name)
        if m:
            return True
        else:
            try:
                m = importlib.import_module(name)
            except ModuleNotFoundError:
                return False
            self.registerModule(r_name, m)
        return True
    def loadModule(self, name, param, r_name):
        return True
