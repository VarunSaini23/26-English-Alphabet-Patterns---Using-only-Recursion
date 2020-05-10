def V(a,b,n):
    if(a-n/2>b):
        return
    print(a*" " + "*" + b*" " + "*")
    V(a+1,b-2,n)
V(0,20,20)
