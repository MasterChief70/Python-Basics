string=input("Enter String =>")
def capitalize_first_last(words):
    words=string.split()
    for i in range(len(words)):
        words[i]=words[i][0].upper()+ words[i][1:-1]+words[i][-1].upper()
    return(' '.join(words))

print(capitalize_first_last(string))