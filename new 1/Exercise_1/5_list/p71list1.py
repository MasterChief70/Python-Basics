import random
list1=[]
n=int(input("Enter Value =>>"))
for i in range(1,n+1):
    x=random.randint(1,50)
    list1.append(x)

print(list1)

for x in list1:
    if x%7==0:
        print(x,",",end="")

