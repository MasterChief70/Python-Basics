from functools import reduce

user_list = list(map(int, input("Enter a list of numbers separated by space: ").split()))
negative_numbers = list(filter(lambda x: x < 0, user_list))
negative_numbers_tuple = tuple(map(lambda x: (x,), negative_numbers))
print("Numbers less than zero:", negative_numbers_tuple)
total_negative_numbers = reduce(lambda x, y: x + y, negative_numbers)
print("Total of all numbers less than zero:", total_negative_numbers)
