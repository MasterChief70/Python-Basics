def CaesarEncryption(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_value = ord(char) + shift
            if char.isupper():
                if shift_value > ord('Z'):
                    shift_value -= 26
                encrypted_text += chr(shift_value)
            else:
                if shift_value > ord('z'):
                    shift_value -= 26
                encrypted_text += chr(shift_value)
        else:
            encrypted_text += char
    return encrypted_text

text = input("Enter Text to Encrypt =>")
shift = int(input("Enter Shift =>"))
cipher = CaesarEncryption(text, shift)
print("Cipher:", cipher)
