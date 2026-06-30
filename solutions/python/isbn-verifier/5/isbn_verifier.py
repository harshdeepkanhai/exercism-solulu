def is_valid(isbn: str) -> bool:
    isbn = list(isbn.replace('-', ''))
    if len(isbn) != 10:
        return False
    
    if isbn[-1] == 'X': 
        isbn[-1] = '10'
    
    if not all(num.isdigit() for num in isbn):
        return False
    return sum((10 - i) * int(num) for i, num in enumerate(isbn)) % 11 == 0