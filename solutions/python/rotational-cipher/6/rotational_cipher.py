from string import ascii_lowercase, ascii_uppercase

def generate_rot_map(rot_map, alpha, key):
    for i in range(len(alpha)):
        rot_map[alpha[i]] = alpha[(i + key) % 26]


def rotate(sentence, key):
    rot_cipher = []
    rot_map = {}
    
    generate_rot_map(rot_map, ascii_lowercase, key)
    generate_rot_map(rot_map, ascii_uppercase, key)
    
    for char in sentence:
        rot_cipher.append(rot_map.get(char, char))
    return ''.join(rot_cipher)