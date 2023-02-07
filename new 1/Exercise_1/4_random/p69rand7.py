import random
x=random.randint(1,40)
y=0
c=0
m=1
n=40
while y!=x:
   y=int(input("Enter number => "))
   c=c+1
   if y<x:
       print("Greater")
       m=y
       print("Range is ", m, "to", n)


   elif y>x:
       print("Smaller")
       n=y
       print("Range is ", m, "to", n)

print("Answer- ",x," You tried ",c,"times")
