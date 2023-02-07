def invert_case(string):
    inverted_string = ""
    for char in string:
        if char.isupper():
            inverted_string += char.lower()
        else:
            inverted_string += char.upper()
    return inverted_string

string = input("Enter a string: ")
print(invert_case(string))
