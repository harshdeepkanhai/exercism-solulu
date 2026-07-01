"""
This module is to find anagram of a word from a list of words 
"""

def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    word: word whose anagram needs to be found
    candidates: list of words from which anagrams need to be found
    """
    return [candidate for candidate in candidates if word.lower() != candidate.lower() and sorted(candidate.lower()) == sorted(word.lower())]
