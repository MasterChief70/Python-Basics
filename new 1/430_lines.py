import random

x_1=input("Enter 1 for tic tac toe, 2 to find prime numbers, 3 to print patterns, 4 to for menu, 5 to view tupple, 6 for fibonacci,"
          " 7 to play KBC, 8 for Calculator, 9 for Math Menu, 10 for xerox shop, 11 to find pelindrome, 12 to find armstrong, "
          "13 to find Krishnamurthy=>")
if x_1==1:
    l1=['_','_','_','_','_','_','_','_','_']
    t=1

    z=input("Enter Who Wants to Start ->").lower()
    while t<10:
        if t%2==0:
            a=int(input("Enter Player 2 =>>"))
            if l1[a-1] =='_':
                l1[a-1]='X'
            else:
                print("Error")
                t=t-1
        elif t%2!=0:
            b=int(input("Enter Player 1 =>>"))
            if l1[b-1]=='_':
                l1[b-1]='O'
            else:
                print("Error")
                t=t-1
        print("After",t,"Turn")
        print(l1[0],l1[1],l1[2])
        print(l1[3],l1[4],l1[5])
        print(l1[6],l1[7],l1[8])
        if l1[0]==l1[1] and l1[0]==l1[2] and l1[0]=='X':
            print("Player 2 Wins")
            t=15
        elif l1[3]==l1[4] and l1[3]==l1[5] and l1[3]=='X':
            print("Player 2 Wins")
            t = 15
        elif l1[6]==l1[7] and l1[6]==l1[8] and l1[6]=='X':
            print("Player 2 Wins")
            t = 15
        elif l1[0]==l1[3] and l1[0]==l1[6] and l1[0]=='X':
            print("Player 2 Wins")
            t = 15
        elif l1[1]==l1[4] and l1[1]==l1[7] and l1[1]=='X':
            print("Player 2 Wins")
            t = 15
        elif l1[2]==l1[5] and l1[2]==l1[8] and l1[2]=='X':
            print("Player 2 Wins")
            t = 15
        elif l1[0]==l1[4] and l1[0]==l1[8] and l1[0]=='X':
            print("Player 2 Wins")
            t = 15
        elif l1[2]==l1[4] and l1[2]==l1[6] and l1[2]=='X':
            print("Player 2 Wins")
            t = 15
        if l1[0]==l1[1] and l1[0]==l1[2] and l1[0]=='O':
            print("Player 1 Wins")
            t = 150
        elif l1[3]==l1[4] and l1[3]==l1[5] and l1[3]=='O':
            print("Player 1 Wins")
            t = 150
        elif l1[6]==l1[7] and l1[6]==l1[8] and l1[6]=='O':
            print("Player 1 Wins")
            t = 150
        elif l1[0]==l1[3] and l1[0]==l1[6] and l1[0]=='O':
            print("Player 1 Wins")
            t = 150
        elif l1[1]==l1[4] and l1[1]==l1[7] and l1[1]=='O':
            print("Player 1 Wins")
            t = 150
        elif l1[2]==l1[5] and l1[2]==l1[8] and l1[2]=='O':
            print("Player 1 Wins")
            t = 150
        elif l1[0]==l1[4] and l1[0]==l1[8] and l1[0]=='O':
            print("Player 1 Wins")
            t = 150
        elif l1[2]==l1[4] and l1[2]==l1[6] and l1[2]=='O':
            print("Player 1 Wins")
            t = 150

        t=t+1

    if t==10:
        print("**********  MATCH DRAW  **********")
    elif t==15:
        print("**********  PLAYER 2 WINS  **********")
    else:
        print("**********  PLAYER 1 WINS  **********")
elif x_1==2:
    n = int(input("Enter Number =>"))
    c = 0
    y = 0
    print("prime numbers are:2,3,")
    for i in range(4, n + 1):
        c = 0
        y = i
        for j in range(2, i):
            if y % j == 0:
                c = 1
                break
        if c == 0:
            print(y, end=",")
elif x_1==3:
    n = int(input("Enter number =>"))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print("")

    n = int(input("Enter number =>"))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print("")

    n = int(input("Enter number =>"))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end="")
        print("")

    n = int(input("Enter number =>"))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j % 2 == 0:
                print("0", end="")
            else:
                print("1", end="")
        print("")

    n = int(input("Enter number =>"))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % 2 == 0:
                print("0", end="")
            else:
                print("1", end="")
        print("")

    n = int(input("Enter number =>"))
    x = 0
    for i in range(1, n + 1):
        if x < n:
            for j in range(1, i + 1):
                x = x + 1
                print(x, end="")
        else:
            break
        print("")
elif x_1==4:
    print("Pizza: 500")
    print("Dosa: 300")
    print("Vada: 100")
    print("All")
    x = input("Enter Food Item =>").lower()
    if x == "pizza":
        n = float(input("Enter Quantity =>"))
        print(n * 500)
    elif x == "dosa":
        n = float(input("Enter Quantity =>"))
        print(n * 300)
    elif x == "vada":
        n = float(input("Enter Quantity =>"))
        print(n * 100)
    elif x == "all":
        n = float(input("Enter Pizza Quantity =>"))
        m = float(input("Enter Dosa Quantity =>"))
        b = float(input("Enter Vada Quantity =>"))
        print("Pizza- ", n * 500)
        print("Dosa- ", m * 300)
        print("Vada- ", b * 100)
        print("Total- ", (n * 500) + (m * 300) + (b * 100))
    else:
        print("Invalid Response")
elif x_1==5:
    tuple1 = (11, 42, 35, 66, 98, 67, 25, 15, 82, 11, 11, 42)
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    c = 0
    b = 0
    for i in tuple1:
        if i % 2 == 0:
            list1.append(i)
            tuple4 = (list1)
            c = c + 1
        else:
            list2.append(i)
            tuple5 = (list2)
            b = b + 1

    print(tuple4)
    print(tuple5)
    print("Even Sum =", sum(tuple4))
    print("Odd Sum =", sum(tuple5))
    print("Even Count =", c, "Odd Count =", b)

    list4 = (list)(tuple1)
    list4.sort()
    tuple2 = (list4)
    print(tuple2)
    list4.reverse()
    tuple3 = (list4)
    print(tuple3)

    x = int(input("Enter Search Value->"))
    print(tuple1.count(x))
elif x_1==6:
    n = int(input("Please enter Range :"))
    c = 0
    v = 1
    for i in range(0, n):
        if i <= 1:
            z = i
        else:
            z = c + v
            c = v
            v = z
        print(z)
elif x_1==7:
    print("What is the current year?")
    print("Option a: 2015")
    print("Option b: 2016")
    print("Option c: 2020")
    print("Option d: 2022")
    x = input("Enter Answer =>").lower()
    if x == "d" or x == "2022":
        print("What Day Is It?")
        print("Option a: Friday")
        print("Option b: Monday")
        print("Option c: Sunday")
        print("Option d: Wednesday")
        n = input("Enter Answer =>").lower()
        if n == "d" or n == "wednesday":
            print("What Month Is Going On?")
            print("Option a: Jan")
            print("Option b: Feb")
            print("Option c: March")
            print("Option d: July")
            m = input("Enter Answer =>").lower()
            if m == "d" or m == "july":
                print("What is Mann's Name?")
                print("Option a: cshjbv")
                print("Option b: tuihi")
                print("Option c: sjbf")
                print("Option d: Mann")
                b = input("Enter Answer =>").lower()
                if b == "d" or b == "mann":
                    print("What is the current weather?")
                    print("Option a: summer")
                    print("Option b: winter")
                    print("Option c: autumn")
                    print("Option d: monsoon")
                    v = input("Enter Answer =>").lower()
                    if v == "d" or v == "monsoon":
                        print("CONGRATULATIONS YOU WIN!!!!")
                    else:
                        print("SORRY WRONG ANSWER")
                else:
                    print("SORRY WRONG ANSWER")
            else:
                print("SORRY WRONG ANSWER")
        else:
            print("SORRY WRONG ANSWER")
    else:
        print("SORRY WRONG ANSWER")
elif x_1==8:
    print("Enter 1  for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    x = int(input("Enter Option =>"))
    if x == 1:

        n = float(input("Enter Number 1 =>"))
        m = float(input("Enter Number 2 =>"))
        print(n + m)
    elif x == 2:

        n = float(input("Enter Number 1 =>"))
        m = float(input("Enter Number 2 =>"))
        print(n - m)
    elif x == 3:

        n = float(input("Enter Number 1 =>"))
        m = float(input("Enter Number 2 =>"))
        print(n * m)
    elif x == 4:

        n = float(input("Enter Number 1 =>"))
        m = float(input("Enter Number 2 =>"))
        print(n / m)
    else:
        print("Enter Valid Option")
elif x_1==9:
    print("Enter 1 for Area of Triangle")
    print("Enter 2 for Max Between Two Number")
    print("Enter 3 for Positive-Negative")
    print("Enter 4 for Max Between Three Numbers")
    x = int(input("Enter Option =>"))
    if x == 1:
        h = float(input("Enter Height of Triagle =>"))
        b = float(input("Enter Base of Triangle =>"))
        print(("Area of Triangle is"), (h * b) / 2)
    elif x == 2:
        n = float(input("Enter Number 1 =>"))
        m = float(input("Enter Number 2 =>"))
        if n > m:
            print(n, ("is Greater"))
        else:
            print(m, ("is Greater"))
    elif x == 3:
        n = float(input("Enter Number 1 =>"))
        if n >= 0:
            print("Positive")
        else:
            print("Negative")
    elif x == 4:
        n = float(input("Enter Number 1 =>"))
        m = float(input("Enter Number 2 =>"))
        b = float(input("Enter Number 3 =>"))
        if n > m and n > b:
            print(n, ("is the Greatest"))
        elif m > n and m > b:
            print(m, ("is the Greatest"))
        else:
            print(b, ("is the Greates"))
    else:
        print("Invalid")
elif x_1==10:
    print("Type: 15 (less than 50 pages) or 12 (more than 50 pages)")
    print("Print: 20 (less than 50 pages) or 17 (more than 50 pages)")
    print("Xerox: 25 (less than 50 pages) or 22 (more than 50 pages)")
    print("ALL")
    x = input("Enter Service Required =>").lower()
    if x == "type":
        n = float(input("Enter Quantity =>"))
        if n <= 50:
            print(n * 15)
        else:
            print(n * 12)
    elif x == "print":
        n = float(input("Enter Quantity =>"))
        if n <= 50:
            print(n * 20)
        else:
            print(n * 17)
    elif x == "xerox":
        n = float(input("Enter Quantity =>"))
        if n <= 50:
            print(n * 25)
        else:
            print(n * 22)
    elif x == "all":
        n = float(input("Enter Typing Quantity =>"))
        m = float(input("Enter Printing Quantity =>"))
        b = float(input("Enter Xerox Quantity =>"))
        t = 0
        if n <= 50:
            t = n * 15
            print(n * 15)
        else:
            t = n * 12
            print(n * 12)
        if m <= 50:
            r = m * 20
            print(m * 20)
        else:
            r = m * 17
            print(m * 17)
        if b <= 50:
            y = b * 25
            print(b * 25)
        else:
            y = b * 22
            print(b * 22)
        print("TOTAL:- ", t + r + y)

    else:
        print("Invalid")
elif x_1==11:
    n = int(input("Enter number =>>"))
    c = n
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    print("Reverse =", rev, "Number:", n)

    if rev == c:
        print("Heck yeah, Number is pelindrome")
    else:
        print("Lmao nope, Not a pelindrome")
elif x_1==12:
    n = int(input("Enter number =>>"))
    c = n
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev + rem * rem * rem
        n = n // 10

    print("End number=", rev, "Number:", c, n)

    if rev == c:
        print("Heck yeah, Number is armstrong")
    else:
        print("Lmao nope, Not a armstrong")
elif x_1==13:
    n = int(input("Enter number =>>"))
    c = n
    rev = 0
    while n > 0:
        rem = n % 10
        f = 1
        for i in range(1, rem + 1):
            f = f * i
        rev = rev + f
        n = n // 10

    print("End number=", rev, "Number:", c, n)

    if rev == c:
        print("Heck yeah, Number is Krishnamurti")
    else:
        print("Lmao nope, Not a Krishnamurti")
else:
    print(" Invalid Input :(")