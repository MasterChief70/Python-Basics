f1=open("d:\\abc.txt","r")
f2=open("d:\\xyz.txt","w")


z=0
while True:
    data=f1.read(1)
    if not data:
        break

    if data==" ":
        z=z+1
        print(data,end="")
        f2.write(data)
    else:
        if z>0:
            print(data.upper(),end="")
            f2.write(data.upper())
        else:
            print(data, end="")
            f2.write(data)
        z=0
f1.close()
f2.close()