BRACKETS = {'(': ')', '[': ']', '{': '}'}
END_BRACKETS = {')', ']', '}'}


def is_paired(input_string):
    stack = []
    
    def is_valid(char):
        return stack and stack.pop() == char
        
    for char in input_string:
        if char in BRACKETS:
            stack.append(BRACKETS[char])
        elif char in END_BRACKETS and not is_valid(char):
            return False
    return not stack