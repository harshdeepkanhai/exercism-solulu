import string


def generate_rot_map(rot_map, alpha, key):
    rot_map.update({chr : alpha[(i + key) % 26] for i, chr in enumerate(alpha)})


def rotate(sentence, key):
    rot_map = {}
    generate_rot_map(rot_map, string.ascii_lowercase, key)
    generate_rot_map(rot_map, string.ascii_uppercase, key)
    return ''.join([ rot_map.get(char, char) for char in sentence ])