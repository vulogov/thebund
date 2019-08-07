##
##
##
from BundCtx import BundCtx

class BundGrammarCtx:
    def process_context(self):
        self.ctx = BundCtx()
    def process_context(self):
        self.ctx = BundCtx()
        for mm in self.models:
            model = self.models[mm]
            for ctx in model.contexts:
                _ctx = self.ctx.createContext(ctx.name, self.ctx)
                for statement in ctx.statements:
                    if statement.__class__.__name__ == 'DataBlock':
                        for d in statement.definitions:
                            _ctx.registerData(d.name, d.value)
                    else:
                        pass
