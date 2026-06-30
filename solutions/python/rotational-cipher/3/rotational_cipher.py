def rotate(sentence, key):
    rot_cipher = []
    upper_a_ascii = 65    # ord('A')
    lower_a_ascii = 97     # ord('a')
    rot_map = dict()
    for char in range(97,123):
        shifted_char = chr(((char - lower_a_ascii + key) % 26) + lower_a_ascii)
        rot_map[chr(char)] = shifted_char

    for char in range(65,91):
        shifted_char = chr(((char - upper_a_ascii + key) % 26) + upper_a_ascii)
        rot_map[chr(char)] = shifted_char
    for char in sentence:
        if char.isalpha():
            rot_cipher.append(rot_map[char])
        else:
            rot_cipher.append(char)
    return ''.join(rot_cipher)