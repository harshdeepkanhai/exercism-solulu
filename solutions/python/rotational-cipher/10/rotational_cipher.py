import string

def rotate(sentence: str, key: str) -> str:
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    rot_map = {char: lower[(i + key) % 26] for i, char in enumerate(lower)} \
    | {char: upper[(i + key) % 26] for i, char in enumerate(upper)}
    return ''.join([rot_map.get(char, char) for char in sentence])