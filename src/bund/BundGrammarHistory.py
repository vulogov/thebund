##
##
##

class BundGrammarHistory:
    def process_history(self):
        self.history={}
        for mm in self.models:
            model = self.models[mm]
            if len(model.history) == 0:
                continue
            helist = []
            for h in model.history:
                helement = {}
                for he in h.story:
                    helement[he.name] = he.he_val
                helist.append(helement)
            self.history[mm] = helist
