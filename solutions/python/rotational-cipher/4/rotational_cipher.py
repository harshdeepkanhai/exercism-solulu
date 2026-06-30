def generate_rot_map(rot_map, alpha, key):
    for char in range(alpha,alpha+26):
        shifted_char = chr(((char - alpha + key) % 26) + alpha)
        rot_map[chr(char)] = shifted_char


def rotate(sentence, key):
    rot_cipher = []
    upper_a_ascii = 65     # ord('A')
    lower_a_ascii = 97     # ord('a')
    rot_map = dict()
    
    generate_rot_map(rot_map, lower_a_ascii, key)
    generate_rot_map(rot_map, upper_a_ascii, key)
    
    for char in sentence:
        if char.isalpha():
            rot_cipher.append(rot_map[char])
        else:
            rot_cipher.append(char)
    return ''.join(rot_cipher)