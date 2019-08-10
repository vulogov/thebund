##
##
##
import sys
from BundGrammarChannel import BundGrammarChannel
from BundGrammarFileChannel import

class BundGrammarChannels:
    def __init__(self, *args):
        self._in = {'stdin': BundGrammarChannel(stream=sys.stdin)}
        self._out = {'stdout': BundGrammarChannel(stream=sys.stdout),
                     'stderr': BundGrammarChannel(stream=sys.stderr)}
        self.std_out_channel = 'stdout'
        self.std_in_channel = 'stdin'
    def process_channels(self):
        for mm in self.models:
            model = self.models[mm]
            for ctx in model.contexts:
                _ctx = self.ctx.createContext(ctx.name, self.ctx)
                for statement in ctx.statements:
                    if statement.__class__.__name__ == 'InBlockDecl':
                        for d in statement.in_chan:
                            _ctx.registerInChannel(d.name, d.value)
                    if statement.__class__.__name__ == 'OutBlockDecl':
                        for d in statement.in_chan:
                            _ctx.registerOutChannel(d.name, d.value)
