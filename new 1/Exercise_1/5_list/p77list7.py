import random
list1=[]
list2=[]
list3=[]
n=int(input("Enter Value =>>"))

for i in range(1,n+1):
    x=int(random.randint(-50,50))
    list1.append(x)

print(list1)
m=int(input("Enter Search Item =>"))
c=list1.count(m)
if c==0:
    print("Not there")
else:
    print(c,"times")