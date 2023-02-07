import re

def sum_avg_digits(string):
    digits = re.findall('\d', string)
    sum_digits = sum(map(int, digits))
    avg_digits = sum_digits / len(digits)
    return sum_digits, avg_digits

string = input("Enter a string: ")
sum_digits, avg_digits = sum_avg_digits(string)
print("Sum is: ", sum_digits)
print("Average is", avg_digits)
