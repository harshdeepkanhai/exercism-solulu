def find_anagrams(word, candidates):
    result = []

    counter_word = dict()
    for char in word.lower():
        counter_word[char] = counter_word.get(char, 0) + 1
    for candidate in candidates:
        counter_candidate = dict()
        for char in candidate.lower():
            counter_candidate[char] = counter_candidate.get(char, 0) + 1
        if counter_candidate == counter_word and word.lower() != candidate.lower():
            result.append(candidate)
    return result
