import time
current=time.localtime(time.time())
print("Year:",current.tm_year)
print("Month:",current.tm_mon)
print("Day:",current.tm_mday)
print("Weekday:",current.tm_wday)
print("Yearday:",current.tm_yday)
print("Date:",current.tm_mday,current.tm_mon,current.tm_year)
print("Time:",current.tm_hour,current.tm_min,current.tm_sec)

x=current.tm_year
if x%4==0:
    print("This year is a leap year")
else:
    print("Not a leap year")

x=current.tm_hour
if x<12:
    print("Time:",current.tm_hour,current.tm_min,current.tm_sec,"am")
else:
    print("Time:",current.tm_hour,current.tm_min,current.tm_sec,"pm")

x=current.tm_hour
if x>12:
    x=x-12
    if x >= 12:
        print("Time:",x, current.tm_min, current.tm_sec, "am")
    else:
        print("Time:",x, current.tm_min, current.tm_sec, "pm")