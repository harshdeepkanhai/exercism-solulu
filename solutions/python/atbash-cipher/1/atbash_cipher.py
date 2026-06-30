import itertools
import string

def batch_string(string):
    result = ""
    for i in range(0, len(string), 5):
        result += string[i:i+5] + " "
    return result.rstrip()

def encode(plain_text):
    plain_text = "".join(text for text in plain_text if text.isalnum())
    plain_text = plain_text.lower().translate(str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1]))
    return batch_string(plain_text)


def decode(ciphered_text):
    return ciphered_text.lower().replace(" ","").translate(str.maketrans(string.ascii_lowercase[::-1], string.ascii_lowercase))
