try:
    a = int(input("Enter no1 =>"))
    b = int(input("Enter no2 =>"))
    c = a / b
    print("Answer = ", c)
except ValueError:
    print("Why u enter String")
except:
    print("Errror")