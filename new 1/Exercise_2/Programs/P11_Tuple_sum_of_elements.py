from functools import reduce

t = tuple(map(int, input("Enter a list of numbers separated by space: ").split()))
even_numbers = tuple(filter(lambda x: x % 2 == 0, t))
odd_numbers = tuple(filter(lambda x: x % 2 != 0, t))
sum_even = reduce(lambda x, y: x+y,even_numbers)
sum_odd = reduce(lambda x, y: x+y,odd_numbers)
print("Sum of even numbers : ", sum_even)
print("Sum of odd numbers : ", sum_odd)
