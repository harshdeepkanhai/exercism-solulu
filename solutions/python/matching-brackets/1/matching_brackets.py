def is_paired(input_string):
    stack = []
    map_pairs = {']':'[',')':'(','}':'{'}
    for char in input_string:
        if char in map_pairs.values():
            stack.append(char)
        elif char in map_pairs :
            if stack and stack[-1] == map_pairs[char]:
                stack.pop()
            else:
                stack.append(char)
        else:
            continue
    return len(stack) == 0 
