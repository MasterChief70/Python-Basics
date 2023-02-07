n=int(input("Enter Number =>"))
c=0
y=0
print("prime numbers are:2,3,")
for i in range(4,n+1):
    c=0
    y=i
    for j in range(2,i):
        if y%j==0:
            c=1
            break
    if c==0:
        print(y,end=",")