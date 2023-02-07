import random
dic1={}
n=int(input("Enter Value =>>"))
c=0
b=0
for i in range(1,n+1):
    k=random.randint(1,1000)
    v=input("Enter Name -").lower()
    dic1[k]=v

print(dic1)
m=input("Enter Name ->").lower()
c=0
for k,v in dic1.items():
    if m==v:
        c=1
        print(k,"\t\t",v,)


print("*" * 30)

if c==0:
    print("Sorry Not Found")

