def word_frequency(string):
    words = string.split()
    frequency = {}
    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

string = input("Enter String =>")
print(word_frequency(string))
