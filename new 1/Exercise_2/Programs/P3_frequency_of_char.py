string=input("Enter String =>")
char1=input("Enter Char =>")
frequency=0
for i in string:
    if(i==char1):
        frequency=frequency+1

print(char1, frequency)