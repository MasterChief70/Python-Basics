def linear_search(L, target):
    for i in range(len(L)):
        if L[i] == target:
            return f"{target} was found at index {i}."
    return f"{target} not found in the list."

L = list(map(int, input("Enter the list of numbers: ").split()))
target = int(input("The number to search for: "))
print(linear_search(L, target))
