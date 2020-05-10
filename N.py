def N(a,n):
    if(a>10):
        return

    print("*" + a*" " + "* "  + (n-a)*" " + "*" )
    N(a+1,n)
N(0,10)
