def add(*a):
    c=0
    for i in a:
        if i%2==0:
            c=c+1
            z=(sum(a))
    print("count =",c)
    print("sum =",z)

add(1,2,3,4,5)
add(1,2,3)
add(1,2)
add(1,2,3,4,5,56,7,8,9)