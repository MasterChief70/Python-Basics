import random
print("Enter 1 for Addition")
print("Enter 2 for Multiplication")
m=int(input("Enter Option =>"))
if  m==1:
    n = int(input("Enter No. of Questions You Want =>"))
    i = 1
    z = 0
    c = 0
    while i <= n:
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print("N0. 1 = ", x, "No. 2 = ", y)
        m = int(input("Enter Sum of Numbers =>"))
        b = x + y
        i = i + 1
        if m == b:
            z = z + 1
        else:
            c = c + 1
    print("No. of correct answers - ", z, "No. of wrong answers - ", c)
elif m==2:
    n = int(input("Enter No. of Questions You Want =>"))
    i = 1
    z = 0
    c = 0
    while i <= n:
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print("N0. 1 = ", x, "No. 2 = ", y)
        m = int(input("Enter Sum of Numbers =>"))
        b = x * y
        i = i + 1
        if m == b:
            z = z + 1
        else:
            c = c + 1
    print("No. of correct answers - ", z, "No. of wrong answers - ", c)
else:
    print("Invalid Option")

