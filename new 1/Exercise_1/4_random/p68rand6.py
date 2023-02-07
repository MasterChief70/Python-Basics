import random
x=random.randint(1,40)
y=0
c=0
while y!=x:
   y=int(input("Enter number => "))
   c=c+1
   if y<x:
       print("Greater")
   elif y>x:
       print("Smaller")

print("Answer- ",x," You tried ",c,"times")
