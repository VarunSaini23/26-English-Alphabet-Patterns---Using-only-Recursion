def R1(b,n):
    if(n<=0):
        return
    else:
        print("*",end=" ")
        if(n<=5 and n>3):
            R1(b+1,n-1)
        elif(n<=3 and n>3):
            R1(b,n-1)
        else:
            R1(b-1,n-1)
        print("*" + b*"  "  +"*" )
def R2(b,n):
    if(n<=0):
        return
    else:
        print("*",end=" ")
        R2(b-1,n-1)
        print("*" + b*"  "  +"*" )    
R1(6,5)
R2(9,5)
