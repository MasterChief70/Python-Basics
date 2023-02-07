n=int(input("Enter Value =>"))
s=0
for i in range(1,n+1):
    print("1/",i,"+",end="")
    x=1/i
    s=x+s
print("\nSum = ",s)