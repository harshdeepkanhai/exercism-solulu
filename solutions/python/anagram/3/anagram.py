"""
This module is to find anagram of a word from a list of words 
"""

def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    word: word whose anagram needs to be found
    candidates: list of words from which anagrams need to be found
    """
    result = []

    counter_word = {}
    for char in word.lower():
        counter_word[char] = counter_word.get(char, 0) + 1
    for candidate in candidates:
        counter_candidate = {}
        for char in candidate.lower():
            counter_candidate[char] = counter_candidate.get(char, 0) + 1
        if counter_candidate == counter_word and word.lower() != candidate.lower():
            result.append(candidate)
    return result
