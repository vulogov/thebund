##
##
##
import types

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
    return bund_data
