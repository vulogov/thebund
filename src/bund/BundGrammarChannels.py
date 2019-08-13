##
##
##


class BundGrammarChannels:
    def process_channels(self):
        for mm in self.models:
            model = self.models[mm]
            for ctx in model.contexts:
                _ctx = self.ctx.createContext(ctx.name, self.ctx)
                for statement in ctx.statements:
                    if statement.__class__.__name__ == 'InBlockDecl':
                        for d in statement.in_chan:
                            _ctx.registerInChannel(d.btype, d.name,  d.attr, d.type, d.ch_name)
                    if statement.__class__.__name__ == 'OutBlockDecl':
                        for d in statement.out_chan:
                            _ctx.registerOutChannel(d.btype, d.name,  d.attr, d.type, d.ch_name)
        self.std_out_channel = 'stdout'
        self.std_in_channel = 'stdin'
