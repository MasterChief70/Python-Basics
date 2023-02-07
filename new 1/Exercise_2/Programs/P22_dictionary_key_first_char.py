def create_dict(string):
    words = string.split()
    word_dict = {}
    for word in words:
        if word[0] in word_dict:
            word_dict[word[0]].append(word)
        else:
            word_dict[word[0]] = [word]
    return word_dict

string = input("Enter a string: ")
result = create_dict(string)
print(result)
