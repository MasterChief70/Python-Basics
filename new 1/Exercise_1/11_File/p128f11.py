f1=open("d:\\abc.txt","r")
f2=open("d:\\pqr.txt","w")
f3=open("d:\\xyz.txt","w")

c=0

while True:
    data=f1.read(1)
    if not data:
        break

    if data.isupper():
        f2.write(data.lower())
    elif data.islower():
        f3.write(data.upper())
    else:
        print(data,end="")

f1.close()
f2.close()
f3.close()

