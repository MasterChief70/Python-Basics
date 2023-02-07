def add(a,b):
    return a+b,a-b,a*b,a/b

def cube(a):
    return a*a*a

def max(a,b):
    if a>b:
        return a
    else:
        return b

a=int(input("Enter Number 1 =>"))
b=int(input("Enter Number 2 =>"))

a,s,m,d=add(a,b)
print("Sum = ",c)


c=cube(a)
print("Cube = ",c)

c=max(a,b)
print("Max = ",c)