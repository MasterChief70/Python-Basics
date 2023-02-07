n=int(input("Enter Value =>"))
x=0
c=0
v=0
b=0
for i in range(1,n+1):
    if i%2==0:
        v=v+1
        x=x+i
        print(i,"is even")
    else:
        b=b+1
        c=c+i
        print(i,"is odd")
print("Total of Odd Numbers =",c," Total of Even Numbers =",x)
print("Count of Odd Number =",b," Count of Even Numbers =",v)
