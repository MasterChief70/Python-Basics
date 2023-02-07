n=int(input("Enter Number =>"))
for i in range(1,n+1):
    k=n+1
    for j in range(1,i+1):
        k=k-1
        print(" ",end="")
    for j in range(k,0,-1):
        print("*"," ",end="")
    print("")


n=int(input("Enter Number =>"))
for i in range(1,n+1):
    k=n+1
    for j in range(1,i+1):
        k=k-1
        print(" ",end="")
    for j in range(k,0,-1):
        print(k,end="")
    print("")



n=int(input("Enter Number =>"))
for i in range(1,n+1):
    k=n+1
    for j in range(1,i+1):
        k=k-1
        print(" ",end="")
    for j in range(k,0,-1):
        print(i,end="")
    print("")



n=int(input("Enter Number =>"))
for i in range(1,n+1):
    k=n+1
    for j in range(1,i+1):
        k=k-1
        print(" ",end="")
    for j in range(n,i-1,-1):
        print(j,end="")
    print("")



n=int(input("Enter Number =>"))
for i in range(1,n+1):
    k=0
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(n+1,i,-1):
        k=k+1
        print(k,end="")
    print("")