def maximo(a, b, c):
    if a >= b and a >= c:
        #print(a)
        return a
    else:
        if b >= c and b >= a:
            #print(b)
            return b
        else:
           #print(c)
           return c

