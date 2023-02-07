def check_password(password):
    if len(password) < 8 or len(password) > 15:
        return "Invalid Password: Password length should be between 8 to 15 characters."

    lower = False
    upper = False
    special = False
    digit = False
    consecutive = False

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            consecutive = True
            break

    for char in password:
        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdigit():
            digit = True
        elif char in "!@#$%^&*":
            special = True
        elif char == " ":
            return "Invalid Password: Password should not contain any space."

    if lower and upper and special and digit and not consecutive:
        return "Valid Password"
    else:
        return "Invalid Password: Password should contain at least one lowercase letter, one uppercase letter, one special character, one digit and should not contain any repeated combination of consecutive 3 characters."


password = input("Enter a password: ")
print(check_password(password))
