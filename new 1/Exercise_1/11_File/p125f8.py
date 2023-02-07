f1=open("d:\\abc.txt","r")
c=0

while True:
    data=f1.read(1)
    if not data:
        break

    if data==" ":
        print("",end="")
        c=c+1
    else:
        print(data,end="")

f1.close()

