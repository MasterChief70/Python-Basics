def add():
    a=int(input("Enter Number 1 for Addition =>"))
    b=int(input("Enter Number 2 for Addition =>"))
    print("Sum =",a+b)

def tbl():
    a=int(input("Enter NUmber for Table=>"))
    for i in range(1,11):
        print(a,"*",i,"=",a*i)

def cube():
    a=int(input("Enter Number for Cube =>"))
    print("Cube =",a*a*a)

def fact():
    a=int(input("Enter Number for Factorial =>"))
    b=1
    for i in range(1,a+1):
        b=b*i
    print("Fact =",b)

def areaoftriangle():
    a=int(input("Enter Height of Triangle =>"))
    b=int(input("Enter Base of Triangle =>"))
    print("Area of Triangle =",(a*b)/2)

def max3():
    a=int(input("Enter First Number =>"))
    b=int(input("Enter Second Number =>"))
    c=int(input("Enter Third Number =>"))
    if a>b and a>c:
        print(a,"Is the greatest number")
    elif b>a and b>c:
        print(b,"Is the greatest number")
    else:
        print(c,"Is the greatest number")

def primeno():
    n = int(input("Enter Number to find if Prime =>"))
    c = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                c = 1
                break
    if c == 1:
        print(n, "Is not a prime number")
    else:
        print(n, "Is a prime number")

def areaofcircle():
    n=int(input("Enter Radius of the Circle =>"))
    print(3.14*n*n)

add()
tbl()
cube()
fact()
areaoftriangle()
max3()
primeno()
areaofcircle()
