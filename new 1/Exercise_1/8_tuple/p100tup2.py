tuple1=(11,42,35,66,98,67,25,15,82,11,11,42)
list1=[]
list2=[]
list3=[]
list4=[]
c=0
b=0
for i in tuple1:
    if i%2==0:
        list1.append(i)
        tuple4=(list1)
        c=c+1
    else:
        list2.append(i)
        tuple5=(list2)
        b=b+1

print(tuple4)
print(tuple5)
print("Even Sum =",sum(tuple4))
print("Odd Sum =",sum(tuple5))
print("Even Count =",c,"Odd Count =",b)



list4=(list)(tuple1)
list4.sort()
tuple2=(list4)
print(tuple2)
list4.reverse()
tuple3=(list4)
print(tuple3)

x=int(input("Enter Search Value->"))
print(tuple1.count(x))
