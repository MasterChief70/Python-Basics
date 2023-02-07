n=int(input("Enter number =>"))
for i in range(1,n+1):
    x=n+1
    for j in range(i,0,-1):
        x=x-1
        print(x,end="")
    print("")




n=int(input("Enter number =>"))
for i in range(1,n+1):
    if n>0:
        for j in range(i, 1, -1):
            print(n, end="")
            n=n-1
    else:
        break
    print("")

