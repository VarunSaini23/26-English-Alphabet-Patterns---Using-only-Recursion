def B(b,n):
    if(n<=0):
        return
    print("*",end=" ")
    if(n<=5 and n>3):
        B(b+1,n-1)
    elif(n<=3 and n>3):
        B(b,n-1)
    else:
        B(b-1,n-1)
    print("*" + b*"  "  +"*" )
B(6,5)
B(6,5)
print(5 *"* " )
