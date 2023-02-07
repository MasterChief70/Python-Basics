import random
list1=[]
list2=[]
n=int(input("Enter Value =>>"))
for i in range(1,n+1):
    x=int(random.randint(-50,50))
    list1.append(x)
    y=x*(-1)
    list2.append(y)

print(list1)
print(list2)
