m = [2, 4, -6, -9, 11, -12, 14, -5, 17, -5, 43, -32]

positive_nums = list(filter(lambda x: x > 0, m))
negative_nums = list(filter(lambda x: x < 0, m))

positive_sum = sum(positive_nums)
negative_sum = sum(negative_nums)

print("Sum of the positive numbers:", positive_sum)
print("Sum of the negative numbers:", negative_sum)
