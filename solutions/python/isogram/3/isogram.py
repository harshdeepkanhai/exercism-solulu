def is_isogram(phrase):
    scrubbed = list(filter(str.isalpha, phrase.lower()))
    return len(scrubbed) == len(set(scrubbed))