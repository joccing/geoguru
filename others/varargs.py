#! /usr/bin/python3.4

def f(*more):
#    print(repr(list(more)))
    d = {"x":1, "y":2, "z":3,"r":4}
    return {k:d[k] for k in more if k in d}

print(f("y","x","z"))
