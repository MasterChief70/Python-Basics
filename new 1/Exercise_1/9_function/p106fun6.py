def add(a,b):
    print(a+b)

def cube(a,b):
    print(a*a*a,b*b*b)

def max(a,b):
    if a>b:
        print(a,"Is Greater")
    else:
        print(b,"Is Greater")

a=int(input("Enter Number 1 =>"))
b=int(input("Enter Number 2 =>"))

add(a,b)
cube(a,b)
max(a,b)