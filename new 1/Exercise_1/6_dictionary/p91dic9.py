import random
dic1={}
n=int(input("Enter Value =>>"))
c=0
for i in range(1,n+1):
    k=random.randint(1,100)
    v=random.randint(0,100)
    dic1[k]=v

print("Rollno\tMark\tStatus")
print("*"*30)
for k,v in dic1.items():
    if v<35:
        print(k,"\t\t",v,"\t\t","fail")
        c=c+1
print("No. of fail students =",c)
print("*"*30)
