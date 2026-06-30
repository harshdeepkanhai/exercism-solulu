import string

def rows(letter: str) -> list[str]:
    count = string.ascii_uppercase.index(letter)
    line_width = 2 * count + 1
    lines = []
    for offset, char in enumerate(string.ascii_uppercase[:count+1]):
            center =  " " * (offset * 2 - 1)
            line = center.join(char * (2 if offset else 1))
            lines.append(f"{line:^{line_width}}")
        
    return lines + lines[-2::-1]