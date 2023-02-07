import random
list1=[]
list2=[]
n=int(input("Enter Value =>>"))

for i in range(1,n+1):
    x=int(random.randint(0,5000))
    list1.append(x)


print(list1)
y=int(input("Enter Number -->"))
for x in list1:
    if x>y:
        print(x)