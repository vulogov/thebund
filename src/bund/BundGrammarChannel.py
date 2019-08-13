##
##
##
import io
import sys

def createInChannel(ctx, btype, name,  attr, ch_type, ch_name):
    _name = name
    if ch_name:
        _name = ch_name
    if _name in ctx._in:
        return True
    if ch_type.lower() == 'file':
        ctx._in[_name] = BundGrammarFileChannel("r", btype, name,  attr, ch_type, ch_name)


def createOutChannel(ctx, btype, name,  attr, ch_type, ch_name):
    _name = name
    if ch_name:
        _name = ch_name
    if _name in ctx._in:
        return True
    if ch_type.lower() == 'file':
        ctx._out[_name] = BundGrammarFileChannel("w", btype, name,  attr, ch_type, ch_name)

def createStandardChannels(ctx):
    ctx._in = {'stdin': BundGrammarChannel({'stream':sys.stdin})}
    ctx._out = {'stdout': BundGrammarChannel({'stream':sys.stdout}),
                 'stderr': BundGrammarChannel({'stream':sys.stderr})}


class BundGrammarChannel:
    def __init__(self, args={}):
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

class BundGrammarFileChannel(BundGrammarChannel):
    def __init__(self, f_mode, btype, name, attr, ch_type, ch_name):
        BundGrammarChannel.__init__(self)
        if not btype:
            btype = ''
        btype = btype.lower()
        if 'raw' in btype:
            f_mode += 'b'
        else:
            f_mode += 't'
        if 'update' in btype:
            f_mode += '+'
        self.name = ch_name
        self.stream = io.open(name, f_mode)
        print(f_mode, btype, name, attr, ch_type, ch_name)
