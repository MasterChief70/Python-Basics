f1=open("d:\\abc.txt","r")
c=0

while True:
    data=f1.read(1)
    if not data:
        break
    print(data,end="")
    if data.isupper():
        c=c+1

f1.close()

print("\nTotal uppers are ",c)