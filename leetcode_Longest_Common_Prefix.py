def set_intsct(lst):
    c=[set(i) for i in lst]
    d= set.intersection(*c)
    e= "".join(map(str,list(d)))
    return e
