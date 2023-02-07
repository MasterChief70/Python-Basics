import re

def is_valid_password(password):
    if len(password) < 8:
        return "Invalid Password: Minimum 8 characters are required."
    if not re.search("[a-z]", password):
        return "Invalid Password: At least one lowercase letter is required."
    if not re.search("[A-Z]", password):
        return "Invalid Password: At least one uppercase letter is required."
    if not re.search("[0-9]", password):
        return "Invalid Password: At least one number is required."
    if not re.search("[_@$]", password):
        return "Invalid Password: At least one of the special characters (_, @, $) is required."
    return "Valid Password"

password = input("Enter a password: ")
print(is_valid_password(password))
