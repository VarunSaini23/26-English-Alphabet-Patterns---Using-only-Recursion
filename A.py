def A(a,b):
    if(b-a>=20):
        return

    if(b-a==10):
        print(a*" " + (b-a-2)*"*")
    else:
        print(a*" " + "*" + (b-a)*" " + "*")

    A(a-1,b+1)
A(10,10)
