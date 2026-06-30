def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
        
    if output_base < 2:
        raise ValueError("output base must be >= 2")
        
    if any(d >= input_base or d < 0 for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
        
    number = sum(d * input_base ** i for i, d in enumerate(digits[::-1]))
    
    new_digits = []
    
    while number:
        number, remainder = divmod(number,output_base)
        new_digits.append(remainder)
        
    return new_digits[::-1] if new_digits else [0]