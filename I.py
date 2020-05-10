def I(a,n):
    if(a==0):
        print("*" * n)
    if(a==10):
        print("*" * n)
        return
    print((n//2+2)*" " + "*")
    I(a+1,n)
I(0,10)
