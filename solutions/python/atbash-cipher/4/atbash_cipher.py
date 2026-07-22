from string import ascii_lowercase

ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1], ' .,')

def encode(plain_text: str) -> str:
    cleaned = [c for c in plain_text.lower() if c.isalnum()]
    shifted = "".join(cleaned).translate(ENCODING)
    return " ".join(shifted[i:i+5] for i in range(0, len(shifted), 5))


def decode(ciphered_text: str) -> str:
    cleaned = [c for c in ciphered_text if c.isalnum()]
    return "".join(cleaned).translate(ENCODING)
