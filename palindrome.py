print("enter the number")
N=int(input("NUMBER="))
if(N<=1000):
 t=N
 rev=0
 while N>0:
    re=N%10
    rev=rev*10+re
    N=N//10
 if(t==rev):
  print("palindrome")
 else:
    print("not a palindrome")

