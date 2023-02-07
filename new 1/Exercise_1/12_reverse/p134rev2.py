n=int(input("Enter number =>>"))
c=n
rev=0
while n>0:
    rem=n%10
    rev=rev+rem*rem*rem
    n=n//10

print("End number=",rev,"Number:",c,n)

if rev==c:
    print("Heck yeah, Number is armstrong")
else:
    print("Lmao nope, Not a armstrong")
