import random
d1={}

n=int(input("Enter Value =>>"))
for i in range(1,n+1):
    k=random.randint(1,99)
    m1 = random.randint(0, 100)
    m2 = random.randint(0, 100)
    m3 = random.randint(0, 100)
    v=m1,m2,m3
    d1[k]=v


print("*"*30)

l1=[]
l2=[]
for k,v in d1.items():
    m1,m2,m3=v
    total=sum(v)
    l1.append(total)
    l2.append(k)
    if m1>=35 and m2>=35 and m3>=35 and total>=150:
        print(k,"\t\t",m1,m2,m3,"\t\t",total,"\tpass")
    else:
        print(k,"\t\t",m1,m2,m3,"\t\t",total,"\tfail")
print("*"*30)
print("Highest scorer -\t",l2[l1.index(max(l1))],"\t\t",max(l1))

for k,v in d1.items():
    m1,m2,m3=v
    total=sum(v)
    if total==max(l1):
        if m1>=35 and m2>=35 and m3>=35 and total>=150:
            print(k,"\t\t",m1,m2,m3,"\t\t",total,"\tpass")
        else:
            print(k,"\t\t",m1,m2,m3,"\t\t",total,"\tfail")
