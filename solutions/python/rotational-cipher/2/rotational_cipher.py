def rotate(sentence, key):
    rot_cipher = []
    upper_a_ascii = ord('A')
    lowe_a_ascii = ord('a')
    for char in sentence:
        if char.isalpha():
            base = upper_a_ascii if char.isupper() else lowe_a_ascii
            shifted_char = chr(((ord(char) - base + key) % 26) + base)
            rot_cipher.append(shifted_char)
        else:
            rot_cipher.append(char)
    return ''.join(rot_cipher)