import random
dic1={}
n=int(input("Enter Value =>>"))
c=0
b=0
for i in range(1,n+1):
    k=random.randint(1,1000)
    v=random.randint(0,100)
    dic1[k]=v

print(dic1)
m=int(input("Enter Rollno. ->"))
c=0
for k,v in dic1.items():
    if m==k:
        c=1
        if v>=45:
            print(k,"\t\t",v,"\t\t","pass")
        else:
            print(k,"\t\t",v,"\t\t","fail")

print("*" * 30)

if c==0:
    print("Sorry Not Found")
