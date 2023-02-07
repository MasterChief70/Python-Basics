n=int(input("Enter Number =>"))
for i in range(n,0,-1):
    k=n+1
    for j in range(1,i+1):
        k=k-1
        print(" ",end="")
    for j in range(k,0,-1):
        print("*"," ",end="")
    print("")
for i in range(1,n+1):
    k=n+1
    for j in range(1,i+1):
        k=k-1
        print(" ",end="")
    for j in range(k,0,-1):
        print("*"," ",end="")
    print("")