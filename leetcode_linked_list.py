def list_add ( list_1, list_2):
    a= int("".join(map(str,list_1)))
    b= int("".join(map(str,list_2)))
    c= [int(i) for i in str(a+b)]
    return c
