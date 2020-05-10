def U(a,b,n):
    if(a<0):
        return
   
    if(a<=10 and a>4):
        print("*" + n*" " + "*")
        U(a-1,b,n)
    elif(a<=4 and a>0):
        print(b*" " + "*" + (n-2*b)*" " + "*")
        U(a-1,b+1,n)
    else:
        print(b*" " + 2*(b-1)*"* ")
        U(a-1,b+1,n)
    
U(10,0,20)
