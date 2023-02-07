print("Enter 1  for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
x=int(input("Enter Option =>"))
if x==1:

    n = float(input("Enter Number 1 =>"))
    m = float(input("Enter Number 2 =>"))
    print(n+m)
elif x==2:

    n = float(input("Enter Number 1 =>"))
    m = float(input("Enter Number 2 =>"))
    print(n-m)
elif x==3:

    n = float(input("Enter Number 1 =>"))
    m = float(input("Enter Number 2 =>"))
    print(n*m)
elif x==4:

    n = float(input("Enter Number 1 =>"))
    m = float(input("Enter Number 2 =>"))
    print(n/m)
else:
    print("Enter Valid Option")