numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

divisible_by_19_or_13 = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, numbers))
print(divisible_by_19_or_13)
