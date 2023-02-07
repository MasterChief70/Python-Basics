import random
dic1={}
n=int(input("Enter Value =>>"))
c=0
b=0
for i in range(1,n+1):
    k=random.randint(1,100)
    v=random.randint(10,100)
    dic1[k]=v

print("Rollno\tMark")
print("*"*30)
print("Press 1 for All Students")
print("Press 2 for Pass Students")
print("Press 3 for Fail Students")
m = int(input("Enter Number"))
for k,v in dic1.items():
    if m==1:
        if v >= 45:
            c = c + 1
            print(k, "\t\t", v, "       pass")
        else:
            b = b + 1
            print(k, "\t\t", v, "        fail")
    elif m==2:
        if v>=45:
            c=c+1
            print(k, "\t\t", v, "       pass")
    elif m==3:
        if v<45:
            b = b + 1
            print(k, "\t\t", v, "        fail")
    else:
        print("Invalid Input")
print("No. of Students who passed =", c)
print("No. of Students who failed =", b)
print("*"*30)
