n = int(input("Please enter Range :"))
c =0
v = 1
for i in range(0, n):
    if i <= 1:
        z = i
    else:
        z = c + v
        c = v
        v = z
    print(z)