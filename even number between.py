print("display in even number between two intervals")
s=int(input("s="))
e=int(input("e="))
for x in range(s+1,e):
    if(x%2==0):
        print(x)
else:
    print("input is invalid")
