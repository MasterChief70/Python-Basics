n=int(input("Enter number =>>"))
c=n
rev=0
while n>0:
    rem=n%10
    rev=rev+rem
    n=n//10

print("Total Sum =",rev,"Number:",n)


