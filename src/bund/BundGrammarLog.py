##
##
##
import logbook

class BundGrammarLog:
    def __init__(self):
        self.level = logbook.DEBUG
        self._log = {}
        self.log = logbook.Logger("theBund")
    def setLogLevel(self, level):
        for i in self._log:
            self._log[i].level = level
    def registerLog(self, name, param, real_name):
        if real_name:
            _name = real_name
        else:
            _name = name
        if name in self._log:
            return True
        if param.lower() == 'stderr':
            self._log[_name] = logbook.StderrHandler(self.level)
        self.log.handlers.append(self._log[_name])
        self.log.debug("Registerd log-handler %s"%_name)
