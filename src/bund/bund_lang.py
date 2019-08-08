##
## Grammar of theBund
##

from textx import metamodel_from_str
from bund_grammar import bund_grammar
from BundGrammarHistory import BundGrammarHistory
from BundGrammarData import BundGrammarData
from BundGrammarCtx import BundGrammarCtx
from BundGrammarModule import BundGrammarModule


class BundGrammar(BundGrammarHistory,
    BundGrammarData,
    BundGrammarCtx,
    BundGrammarModule):
    def __init__(self):
        self.tx = bund_grammar
        self.meta_model = metamodel_from_str(self.tx, ignore_case=True)
        self.models = {}
        BundGrammarCtx.__init__(self)
    def model(self, name, model):
        self.models[name] = self.meta_model.model_from_str(model)


if __name__ == '__main__':
    bg = BundGrammar()
    bg.model("1", open("../../examples/1.bund").read())
    bg.model("2", open("../../examples/2.bund").read())
    bg.model("3", open("../../examples/3.bund").read())
    bg.model("4", open("../../examples/4.bund").read())

    bg.process_history()
    bg.process_environment()
    bg.process_context()
