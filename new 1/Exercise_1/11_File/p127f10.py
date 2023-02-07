f1=open("d:\\abc.txt","r")
f2=open("d:\\pqr.txt","w")

while True:
    data=f1.read(1)
    if not data:
        break

    f2.write(data)
f1.close()
f2.close()

print("Copied")

