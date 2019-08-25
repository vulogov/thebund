##
##
##
import types

CODEBLOCKREF    = 0
CODEBLOCK        = 1
CODEWORDLAZY     = 2
CODEWORDLAZYEVAL = 3

def bund2python(ctx, bund_data):
    if type(bund_data) == type("") and ctx[bund_data] != None:
        return ctx[bund_data]
    #if type(bund_data) == type("") and "->"
    if type(bund_data) in [type(0), type(""), type(0.0)]:
        return bund_data
    if bund_data.__class__.__name__ == "List":
        _d = []
        for le in bund_data.value:
            _d.append(bund2python(ctx, le))
        return _d
    if bund_data.__class__.__name__ == "KV":
        _d = {}
        for kv in bund_data.kvalue:
            _d[kv.name] = bund2python(ctx, kv.value)
        return _d
    if bund_data.__class__.__name__ == "CodeBlockRef":
        _d = []
        for w in bund_data.words:
            _d.append(bund2python(ctx, w))
        return (CODEBLOCKREF,_d, bund_data.arity)
    if bund_data.__class__.__name__ == "CodeBlock":
        _d = []
        for w in bund_data.words:
            _w = bund2python(ctx, w)
            if _w != None:
                _d.append(_w)
            else:
                ctx.parser.log.warning("NOOP detected")
        return (CODEBLOCK,_d, bund_data.arity)
    if bund_data.__class__.__name__ == "CodeWordLazy":
        return (CODEWORDLAZY, bund_data.word)
    if bund_data.__class__.__name__ == "CodeLazyEval":
        return (CODEWORDLAZYEVAL, bund_data.name)
    if bund_data.__class__.__name__ == "CodeWordWReferenceOnModule":
        res = ctx.DATA(bund_data.module, bund_data.fun)
        if not res:
            ctx.parser.log.warning("Data: /{}->{} not found for an early binding", bund_data.module, bund_data.fun)
        return res
    return bund_data
