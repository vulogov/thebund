##
##
##
import types

CODEBLOCKREF    = 0
CODEBLOCK        = 1
CODEWORDLAZY     = 2
CODEWORDLAZYEVAL = 3

def bund2python(bund_data):
    if type(bund_data) in [type(0), type(""), type(0.0)]:
        return bund_data
    if bund_data.__class__.__name__ == "List":
        _d = []
        for le in bund_data.value:
            _d.append(bund2python(le))
        return _d
    if bund_data.__class__.__name__ == "KV":
        _d = {}
        for kv in bund_data.kvalue:
            _d[kv.name] = bund2python(kv.value)
        return _d
    if bund_data.__class__.__name__ == "CodeBlockRef":
        _d = []
        for w in bund_data.words:
            _d.append(bund2python(w))
        return (CODEBLOCKREF,_d, bund_data.arity)
    if bund_data.__class__.__name__ == "CodeBlock":
        _d = []
        for w in bund_data.words:
            _d.append(bund2python(w))
        return (CODEBLOCK,_d, bund_data.arity)
    if bund_data.__class__.__name__ == "CodeWordLazy":
        return (CODEWORDLAZY, bund_data.word)
    if bund_data.__class__.__name__ == "CodeLazyEval":
        return (CODEWORDLAZYEVAL, bund_data.name)

    return bund_data
