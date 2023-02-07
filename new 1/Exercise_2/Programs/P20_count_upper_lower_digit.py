def count_case_and_digits(string):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
    return upper_count, lower_count, digit_count

string = input("Enter a string: ")
upper, lower, digits = count_case_and_digits(string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
print("Number of digits:", digits)
