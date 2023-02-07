import random
dic1={}
n=int(input("Enter Value =>>"))
for i in range(1,n+1):
    k=random.randint(1,50)
    v=random.randint(35,100)
    dic1[k]=v

print(dic1)
