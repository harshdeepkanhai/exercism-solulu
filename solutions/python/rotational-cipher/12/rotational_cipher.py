import string


def rotate(sentence: str, key: str) -> str:
    rot_map = {
        char: string.ascii_lowercase[(i + key) % 26] for i, char in enumerate(string.ascii_lowercase)} | {
        char: string.ascii_uppercase[(i + key) % 26] for i, char in enumerate(string.ascii_uppercase)
    }
    return ''.join(rot_map.get(char, char) for char in sentence)