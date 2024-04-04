import sys
#light ==> life
#0 = l = same
#1 = i = same
#2&3 = gh = f  ==> distance between g and h, to minus
#4 = t = e ==> 15 or 2&3 - 1
x = []
for i in range(len(sys.argv[1])):
    if (i%len(sys.argv[1]) == (0|1)):
        print(sys.argv[1][i], end="")
    elif (i% len(sys.argv[1]) == (2|3)):
        x.append(ord(sys.argv[1][i]))
        if len(x) == 2:
            v = chr(ord(x[0])-ord(x[1])+97)
            print(v, end="")
            x = []
    else:
        G = ord(sys.argv[2][0]) #e
        T = ord(sys.argv[1][i])
        print(chr(G-T+97), end="")

ImportWarning.with_traceback.__class__
import _imp
try:
    _imp.get_frozen_object(str(_imp.acquire_lock(_imp.create_dynamic())))
except:
    import db
    db.__loader__.__dir__