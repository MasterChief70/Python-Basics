import random
list1=[]
list2=[]
list3=[]
n=int(input("Enter Value =>>"))
c=0

for i in range(1,n+1):
    x=int(random.randint(-50,50))
    list1.append(x)


print(list1)
m=int(input("Enter Number ->"))
for i in list1:
    if m==i:
        c=c+1

print("Count of Search =",c)


