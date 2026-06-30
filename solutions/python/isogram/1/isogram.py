def is_isogram(string):
    counter = {}
    for char in string.lower():
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
    return all(i == 1 for i in counter.values())
