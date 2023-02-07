import random
list1=[]
list2=[]
list3=[]
n=int(input("Enter Value =>>"))
for i in range(1,n+1):
    x=int(random.randint(-50,50))
    list1.append(x)
    y=x
    if y%2==0:
        list2.append(y)
    else:
        list3.append(y)
print(list1)
print(list2)
print(list3)

