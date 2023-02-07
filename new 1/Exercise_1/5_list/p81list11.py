import random
list1=[]
list2=[]
n=int(input("Enter Value =>>"))

for i in range(1,n+1):
    x=int(random.randint(0,50))
    list1.append(x)

print(list1)
list2.append(list1)
print(list2)
