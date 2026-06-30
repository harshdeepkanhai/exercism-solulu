UPPER_A_ASCII = ord('A')
LOWER_A_ASCII = ord('a')

def generate_rot_map(rot_map, alpha, key):
    for char in range(alpha,alpha+26):
        shifted_char = chr(((char - alpha + key) % 26) + alpha)
        rot_map[chr(char)] = shifted_char
def rotate(sentence, key):
    rot_cipher = []
    rot_map = {}
    
    generate_rot_map(rot_map, LOWER_A_ASCII, key)
    generate_rot_map(rot_map, UPPER_A_ASCII, key)
    
    for char in sentence:
        rot_cipher.append(rot_map.get(char,char))
    return ''.join(rot_cipher)