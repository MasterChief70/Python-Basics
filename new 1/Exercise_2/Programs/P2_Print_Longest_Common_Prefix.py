list1=["lessonplan", "lesson","ees", "length"]
def longest_common_prefix(strings):
    if not strings:
        return -1
    if len(strings) == 1:
        return strings[0]
    strings.sort()
    first = strings[0]
    last = strings[-1]
    for i, char in enumerate(first):
        if char != last[i]:
            if i==0:
                return -1
            else:
                return first[:i]
    return first

print(longest_common_prefix(list1))
