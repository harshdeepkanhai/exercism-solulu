

def rotate(sentence, key):
    rot_cipher = ""
    for char in sentence:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr(((ord(char) - base + key) % 26) + base)
            rot_cipher += shifted_char
        else:
            rot_cipher += char
    return rot_cipher