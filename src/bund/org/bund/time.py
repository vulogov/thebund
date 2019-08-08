##
##
##

def now(ctx):
    import time
    ctx.push(time.time())
    return ctx
