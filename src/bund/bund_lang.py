##
## Grammar of theBund
##

from textx import metamodel_from_str
from bund_grammar import bund_grammar
from BundGrammarHistory import BundGrammarHistory
from BundGrammarCtx import BundGrammarCtx
from BundGrammarModule import BundGrammarModule
from BundGrammarQueue import BundGrammarQueue
from BundGrammarChannels import BundGrammarChannels
from BundGrammarLog import BundGrammarLog
from BundGrammarExecutive import BundGrammarExecutive



class BundGrammar(BundGrammarHistory,
    BundGrammarCtx,
    BundGrammarModule,
    BundGrammarQueue,
    BundGrammarChannels,
    BundGrammarLog,
    BundGrammarExecutive):
    def __init__(self):
        self.tx = bund_grammar
        self.meta_model = metamodel_from_str(self.tx, ignore_case=True)
        self.models = {}
        BundGrammarCtx.__init__(self)
        BundGrammarQueue.__init__(self)
        BundGrammarChannels.__init__(self)
        BundGrammarLog.__init__(self)
        BundGrammarExecutive.__init__(self)

    def model(self, name, model):
        self.models[name] = self.meta_model.model_from_str(model)


if __name__ == '__main__':
    bg = BundGrammar()
    bg.model("1", open("../../examples/1.bund").read())
    bg.model("2", open("../../examples/2.bund").read())
    bg.model("3", open("../../examples/3.bund").read())
    bg.model("4", open("../../examples/4.bund").read())
    bg.model("5", open("../../examples/5.bund").read())
    bg.model("6", open("../../examples/6.bund").read())
    bg.model("7", open("../../examples/7.bund").read())

    bg.process_history()
    bg.process_environment()
    bg.process_channels()
    bg.process_context()
    print(bg.ctx("Six").getInChannel("passwd"))
    bg.C("Main")
    bg.EVAL("Seven->Main")
