n=int(input("Enter Range End =>"))
m=int(input("Enter Numbber =>"))
for i in range(1,n+1):
    if i%m==0:
        print(i,"is divisible by",m)
    else:
        print(i,"is not divisible by",m)
