from string import ascii_lowercase

ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1], " .,")

def encode(plain_text: str) -> str:
    shifted = "".join(plain_text.lower()).translate(ENCODING)
    return " ".join(shifted[i:i+5] for i in range(0, len(shifted), 5))


def decode(ciphered_text: str) -> str:
    return "".join(ciphered_text).translate(ENCODING)
