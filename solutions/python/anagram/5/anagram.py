"""
This module is to find anagram of a word from a list of words 
"""

def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    word: word whose anagram needs to be found
    candidates: list of words from which anagrams need to be found
    """

    word = word.lower()
    rep = sorted(word)
    pairs = [(candidate, candidate.lower()) for candidate in candidates]
    return [candidate for candidate, candidate_lower in pairs 
            if word != candidate_lower and rep == sorted(candidate_lower)]
