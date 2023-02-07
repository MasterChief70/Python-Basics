import random
list1=[]
n=int(input("Enter Value =>>"))
c=0
v=0
b=0
m=0
for i in range(1,n+1):
    x=random.randint(1,50)
    list1.append(x)

print(list1)

for x in list1:
    if x%2==0:
        print(x,"is Odd")
        c=c+x
        b=b+1
    else:
        print(x,"is Even")
        v=v+x
        m=m+1

print("Sum of Even =",c,"Sum of Odd =",v)
print("Count of Even =",b,"Count of Odd",m)
