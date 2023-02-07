print("Enter a for Area of Triangle")
print("Enter m for Max Between Two Number")
print("Enter p for Positive-Negative")
print("Enter t for Max Between Three Numbers")
x=input("Enter Option =>")
if x=="a":
    h=float(input("Enter Height of Triagle =>"))
    b=float(input("Enter Base of Triangle =>"))
    print(("Area of Triangle is"),(h*b)/2)
elif x=="m":
    n=float(input("Enter Number 1 =>"))
    m=float(input("Enter Number 2 =>"))
    if n>m:
        print(n, ("is Greater"))
    else:
        print(m, ("is Greater"))
elif x=="p":
    n=float(input("Enter Number 1 =>"))
    if n>=0:
        print("Positive")
    else:
        print("Negative")
elif x == "t":
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


