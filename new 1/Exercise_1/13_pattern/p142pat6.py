n=int(input("Enter number =>"))
for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print("*",end="")
    print("")

n = int(input("Enter number =>"))
for i in range(1, n + 1):
    for j in range(n, i-1, -1):
        print(j, end="")
    print("")

n = int(input("Enter number =>"))
for i in range(1, n + 1):
    x=1
    for j in range(n + 1, i, -1):
        print(x, end="")
        x=x+1
    print("")

n = int(input("Enter number =>"))
x=n+1
for i in range(1, n + 1):
    x=x-1
    for j in range(n + 1, i, -1):
        print(x, end="")
    print("")



n = int(input("Enter number =>"))
for i in range(1, n + 1):
    for j in range(n + 1, i, -1):
        print(i, end="")
    print("")



