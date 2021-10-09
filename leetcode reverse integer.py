def rvrs_int (i):
    if i>0:
        d=[b for b in str(i)]
        d.reverse()
        i= int("".join(d))
        if i>(2**31)-1:
            i=0
        return i
    elif i<0:
        k= str(abs(i))
        k=k[::-1]
        i = int(('-'+k))
        if i<(-2**31):
            i=0
        return i
    
        
