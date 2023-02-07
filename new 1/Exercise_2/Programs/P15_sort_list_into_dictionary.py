from collections import defaultdict

def group_elements(lst):
    d = defaultdict(list)
    for i in lst:
        d[i].append(i)
    return dict(sorted(d.items()))

test_list = list(map(int, input("Enter a list of numbers separated by space: ").split()))
print(group_elements(test_list))
