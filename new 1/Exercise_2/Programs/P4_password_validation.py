def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    return has_upper and has_lower and has_digit

password = input("Enter a password: ")
if is_valid_password(password):
    print("The password is valid.")
else:
    print("The password is not valid.")
