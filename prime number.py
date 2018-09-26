print("enter the number")
N=int(input("NUMBER="))
flag=0
for x in range (1,N+1) :
    if(N%x==0):
        flag=flag+1
if(flag==2):
 print("PRIME")
else:
    print("NOT A PRIME")
