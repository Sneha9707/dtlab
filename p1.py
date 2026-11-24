x=1
n=int(input("enter the rows"))
for i in range(1,n+1):
    for j in range(i):
        print(x,end=" ")
        x=x+1
    print()