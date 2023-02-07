import random
y=random.randint(1,6)
a=0
b=0
print(y)
while a<=100 or b<=100:
    x=random.randint(1,6)
    a=a+x
    print("Player 1 score - ",a)
    n=random.randint(1,6)
    b=b+n
    print("Player 2 score - ",b)
    if a>=100:
        print("Winner is Player 1")
    elif b>=100:
        print("Winner is Player 2")

