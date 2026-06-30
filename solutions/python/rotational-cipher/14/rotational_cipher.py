import string


def rotate(text: str, key: str) -> str:
    translator = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    return text.translate(str.maketrans(string.ascii_lowercase+string.ascii_uppercase, translator + translator.upper()))