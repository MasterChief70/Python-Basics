import random
dic1={}
n=int(input("Enter Value =>>"))
for i in range(1,n+1):
    k=random.randint(1,100)
    v=random.randint(35,100)
    dic1[k]=v

print("Rollno\tMark")
print("*"*30)
for k,v in dic1.items():
    print(k,"\t\t",v)
print("*"*30)
