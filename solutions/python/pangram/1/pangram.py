def is_pangram(sentence):
    counter = [0] * 26
    for char in sentence.lower():
        if char.isalpha():
            counter[ord(char) - ord('a')] += 1
    return all(i >= 1 for i in counter)
