f1=open("d:\\abc.txt","r")
f2=open("d:\\pqr.txt","r")
f3=open("d:\\xyz.txt","w")

c=0
while True:
    data=f1.read(1)
    if not data:
        break
    f3.write(data)

while True:
    data=f2.read(1)
    if not data:
        break
    f3.write(data)

f1.close()
f2.close()
f3.close()