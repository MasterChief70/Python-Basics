def is_balanced(string1, string2):
    for char in string1:
        if char not in string2:
            return False
    return True

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if is_balanced(string1, string2):
    print("The two strings are balanced.")
else:
    print("The two strings are not balanced.")
