n=int(input("Enter number =>"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print("")



n=int(input("Enter number =>"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")



n=int(input("Enter number =>"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print("")


n=int(input("Enter number =>"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print("")



n=int(input("Enter number =>"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print("")




n=int(input("Enter number =>"))
x=0
for i in range(1,n+1):
    if x<n:
        for j in range(1, i + 1):
            x = x + 1
            print(x, end="")
    else:
        break
    print("")


