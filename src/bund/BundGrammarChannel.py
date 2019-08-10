##
##
##

class BundGrammarChannel:
    def __init__(self, args):
        self.args = {}
        self.stream = None
        for k in args:
            self.args[k] = args[k]
            if k == 'stream':
                self.stream = args[k]
    def read(self):
        return self.stream.read()
    def write(self, data):
        return self.stream.write(data)
    def readline(self):
        return self.stream.readline()
    def close(self):
        self.stream.close()
