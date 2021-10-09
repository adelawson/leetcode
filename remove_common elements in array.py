def rmv(i):
    i[:]= list(set(i))
    i.sort()
    k= len(i)
    print (i)
    return k
