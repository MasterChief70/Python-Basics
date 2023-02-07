n=int(input("Enter number =>>"))
c=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10

print("Reverse =",rev,"Number:",n)

if rev==c:
    print("Heck yeah, Number is pelindrome")
else:
    print("Lmao nope, Not a pelindrome")
