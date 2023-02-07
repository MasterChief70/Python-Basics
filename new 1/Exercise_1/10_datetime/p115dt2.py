import time
print("This is printed immediately")
time.sleep(2.9)
print("This is printed after 6.9 secs")



now=time.time()
a=input("Enter Name =>")
later=time.time()
difference=int(later-now)
print(difference)