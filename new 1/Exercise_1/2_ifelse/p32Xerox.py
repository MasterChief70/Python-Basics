print("Type: 15 (less than 50 pages) or 12 (more than 50 pages)")
print("Print: 20 (less than 50 pages) or 17 (more than 50 pages)")
print("Xerox: 25 (less than 50 pages) or 22 (more than 50 pages)")
print("ALL")
x=input("Enter Service Required =>").lower()
if x=="type":
    n=float(input("Enter Quantity =>"))
    if n<=50:
        print(n*15)
    else:
        print(n*12)
elif x=="print":
    n=float(input("Enter Quantity =>"))
    if n<=50:
        print(n*20)
    else:
        print(n*17)
elif x=="xerox":
    n=float(input("Enter Quantity =>"))
    if n<=50:
        print(n*25)
    else:
        print(n*22)
elif x=="all":
    n=float(input("Enter Typing Quantity =>"))
    m=float(input("Enter Printing Quantity =>"))
    b=float(input("Enter Xerox Quantity =>"))
    t=0
    if n<=50:
        t=n*15
        print(n*15)
    else:
        t=n*12
        print(n*12)
    if m<=50:
        r=m*20
        print(m*20)
    else:
        r=m*17
        print(m*17)
    if b<=50:
        y=b*25
        print(b*25)
    else:
        y=b*22
        print(b*22)
    print("TOTAL:- ",t+r+y)

else:
    print("Invalid")



