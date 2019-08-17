##
##
##
import sys

def parseArgv():
    d = {'N':[]}
    for i in sys.argv[1:]:
        if '--' in i:
            i.replace('--', '')
            if '=' in i:
                k, v = i.split("=")
                d[k]=v
            else:
                d[i]=True
        else:
            d['N'].append(i)
    return d
