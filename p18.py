print("enter the number")
b=int(input("begin="))
e=int(input("end="))
for x in range(b+1,e):
    s = 0
    a = 0
    t=x
    while x>0:
            re=x%10
            a=re**3
            s=s+a
            x = x // 10
    if(t==s):
         print(s)
