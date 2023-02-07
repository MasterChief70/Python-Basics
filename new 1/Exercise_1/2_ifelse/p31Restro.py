print("Pizza: 500")
print("Dosa: 300")
print("Vada: 100")
print("All")
x=input("Enter Food Item =>").lower()
if x=="pizza":
    n=float(input("Enter Quantity =>"))
    print(n*500)
elif x=="dosa":
    n=float(input("Enter Quantity =>"))
    print(n*300)
elif x=="vada":
    n=float(input("Enter Quantity =>"))
    print(n*100)
elif x=="all":
    n=float(input("Enter Pizza Quantity =>"))
    m=float(input("Enter Dosa Quantity =>"))
    b=float(input("Enter Vada Quantity =>"))
    print("Pizza- ",n*500)
    print("Dosa- ",m*300)
    print("Vada- ",b*100)
    print("Total- ",(n*500)+(m*300)+(b*100))
else:
    print("Invalid Response")
