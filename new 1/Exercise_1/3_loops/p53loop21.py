n=int(input("Enter Value =>"))
s=0
for i in range(1,n+1,2):
        print(i," + ",end="")
        s=s+i
print("\nSum = ",s)
