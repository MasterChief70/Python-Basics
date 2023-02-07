print("Enter 1 for Area of Triangle")
print("Enter 2 for Max Between Two Number")
print("Enter 3 for Positive-Negative")
print("Enter 4 for Max Between Three Numbers")
x=int(input("Enter Option =>"))
if x==1:
    h=float(input("Enter Height of Triagle =>"))
    b=float(input("Enter Base of Triangle =>"))
    print(("Area of Triangle is"),(h*b)/2)
elif x==2:
    n=float(input("Enter Number 1 =>"))
    m=float(input("Enter Number 2 =>"))
    if n>m:
        print(n, ("is Greater"))
    else:
        print(m, ("is Greater"))
elif x==3:
    n=float(input("Enter Number 1 =>"))
    if n>=0:
        print("Positive")
    else:
        print("Negative")
elif x == 4:
    n = float(input("Enter Number 1 =>"))
    m = float(input("Enter Number 2 =>"))
    b = float(input("Enter Number 3 =>"))
    if n>m and n>b:
        print(n,("is the Greatest"))
    elif m>n and m>b:
        print(m, ("is the Greatest"))
    else:
        print(b, ("is the Greates"))
else:
    print("Invalid")


