n=int(input("Enter Number =>"))
c=0
if n>1:
    for i in range(2,n):
        if n%i==0:
            c=1
            break

if c==1:
    print(n,"Is not a prime number")
else:
    print(n,"Is a prime number")






