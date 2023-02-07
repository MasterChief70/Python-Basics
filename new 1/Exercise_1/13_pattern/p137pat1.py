n=int(input("Enter Number for vertical =>"))

for i in range(1,n+1):
    print("*")

n=int(input("Enter Number for horizontal =>"))

for i in range(1,n+1):
    print("*",end="")


n=int(input("\nEnter Number for rectangle =>"))

for i in range(1,n+1):
    print("*"*n)