##
##
##
from BundCtx import BundCtx

class BundGrammarCtx:
    def __init__(self):
        self.ctx = BundCtx('__root__', None, self)
    def process_environment(self):
        for mm in self.models:
            model = self.models[mm]
            for e in model.env:
                for ei in e.envstatement:
                    if ei.type.lower() == 'module':
                        self.loadModule(ei.name, ei.param, ei.real_name)
                    elif ei.type.lower() == 'python':
                        self.loadPythonModule(ei.name, ei.param, ei.real_name)
                    elif ei.type.lower() == "log":
                        self.registerLog(ei.name, ei.param, ei.real_name)
                    else:
                        pass
    def process_context(self):
        for mm in self.models:
            model = self.models[mm]
            for ctx in model.contexts:
                _ctx = self.ctx.createContext(ctx.name, self.ctx)
                for statement in ctx.statements:
                    self.log.debug("Found statement %s"%repr(statement))
                    if statement.__class__.__name__ == 'DataBlock':
                        for d in statement.definitions:
                            _ctx.registerData(d.name, d.value)
                    if statement.__class__.__name__ == 'VarBlock':
                        for d in statement.definitions:
                            _ctx.registerVar(d.name, d.value)
                    if statement.__class__.__name__ == 'CodeBlockDecl':
                        _ctx.registerCode(statement.name, statement.codeblock)
