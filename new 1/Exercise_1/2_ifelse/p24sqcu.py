print("Enter 1 for square")
print("Enter 2 for cube")
x=int(input("Enter option =>"))

if x==1:
    n=float(input("Enter Number =>"))
    print("square = ",n*n)
elif x==2:
    n = float(input("Enter Number =>"))
    print("cube = ", n * n * n)
else:
    print("Wrong opt")