print("Enter add for Addition")
print("Enter sub for Subtraction")
print("Enter mul for Multiplication")
print("Enter div for Division")
x=input("Enter Option =>").lower()
if x=="add":
    n=float(input("Enter Number 1 =>"))
    m=float(input("Enter Number 2 =>"))
    print(n+m)
elif x=="sub":
    n=float(input("Enter Number 1 =>"))
    m=float(input("Enter Number 2 =>"))
    print(n-m)
elif x=="mul":
    n=float(input("Enter Number 1 =>"))
    m=float(input("Enter Number 2 =>"))
    print(n*m)
elif x=="div":
    n=float(input("Enter Number 1 =>"))
    m=float(input("Enter Number 2 =>"))
    print(n/m)
else:
    print("Invalid :(")