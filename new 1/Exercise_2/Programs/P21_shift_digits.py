def shift_and_wrap(n, shift):
    n = str(n)
    if shift > len(n):
        return n[::-1]
    else:
        return n[shift:] + n[:shift]

n = int(input("Enter a number: "))
shift = int(input("Enter the number of places to shift: "))
print("Result:", shift_and_wrap(n, shift))
