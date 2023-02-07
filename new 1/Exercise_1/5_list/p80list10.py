import random
list1=[]
list2=[]
list3=[]
n=int(input("Enter Value =>>"))


for i in range(1,n+1):
    x=int(random.randint(0,5000))
    list1.append(x)

print(list1)
list1.sort()
c=list1[0]
print(list1[0])
list1.reverse()
print(list1[0])
m=list1[0]
z=c+m
print(z)