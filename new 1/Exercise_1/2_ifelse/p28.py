print("Enter sq for Square ")
print("Enter cu for Cube ")
x=input("Enter option =>")
if x=="sq":
    n=float(input("Enter Number =>"))
    print(n*n)
elif x=="cu":
    n=float(input("Enter Number =>"))
    print(n*n*n)
else:
    print("Invalid")