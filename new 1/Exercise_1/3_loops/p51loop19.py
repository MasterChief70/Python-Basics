n=int(input("Enter Value =>"))
s=0
for i in range(1,n+1):
    if i%2==0:
        x = i * i
    else:
        x=i*i*i
    print(x," + ",end="")
    s=s+x
print("\nSum = ",s)

