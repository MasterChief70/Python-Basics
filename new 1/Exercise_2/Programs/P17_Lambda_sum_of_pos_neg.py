from functools import reduce

numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

positive_numbers = list(filter(lambda x: x > 0, numbers))
negative_numbers = list(filter(lambda x: x < 0, numbers))

sum_positive_numbers = reduce(lambda x, y: x + y, positive_numbers)
sum_negative_numbers = reduce(lambda x, y: x + y, negative_numbers)

print("Sum of the positive numbers:", sum_positive_numbers)
print("Sum of the negative numbers:", sum_negative_numbers)
