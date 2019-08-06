##
## Grammar of theBund
##

from textx import metamodel_from_str
from bund_grammar import bund_grammar
from BundGrammarHistory import BundGrammarHistory
from BundGrammarData import BundGrammarData
from BundGrammarCtx import BundGrammarCtx


class BundGrammar(BundGrammarHistory,
    BundGrammarData,
    BundGrammarCtx):
    def __init__(self):
        self.tx = bund_grammar
        self.meta_model = metamodel_from_str(self.tx)
        self.models = {}
    def model(self, name, model):
        self.models[name] = self.meta_model.model_from_str(model)


if __name__ == '__main__':
    bg = BundGrammar()
    bg.model("1", open("../../examples/1.bund").read())
    bg.process_history()
