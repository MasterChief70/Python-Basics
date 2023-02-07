import random
d1={}

n=int(input("Enter Value =>>"))
for i in range(1,n+1):
    k=random.randint(1,99)
    m1 = random.randint(0, 100)
    v=m1
    d1[k]=v
print(d1)

y=int(input("Enter Deletion key -->"))
d1.pop(y)
print(d1)