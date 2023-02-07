n=int(input("Enter number =>>"))
c=n
rev=0
while n>0:
    rem=n%10
    f=1
    for i in range(1,rem+1):
        f=f*i
    rev=rev+f
    n=n//10

print("End number=",rev,"Number:",c,n)

if rev==c:
    print("Heck yeah, Number is Krishnamurti")
else:
    print("Lmao nope, Not a Krishnamurti")

