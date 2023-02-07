n=int(input("Enter Range End =>>"))
m=int(input("Enter Value =>"))
x=0
t=0
for i in range(1,n+1):
    if i%m==0:
        x=x+1
        t=t+i
        print(i,"is divisible by",m)

print("count = ",x," Sum = ",t)