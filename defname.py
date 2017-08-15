# -*- coding: utf-8 -*-
def names(s):
    def name(s):
        return (s[0].upper()+s[1:].lower())
    x=[]
    for p in s:
        x.append(name(p))
    return x

    # map
    # return list(map(name,s))