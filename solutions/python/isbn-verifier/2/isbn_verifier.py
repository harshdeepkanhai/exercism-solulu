def is_valid(isbn):
    isbn = isbn.replace('-', '')
    isbn_product_sum = 0
    
    if len(isbn) != 10 or not isbn[-1].isdigit() and isbn[-1] != 'X':
        return False
    isbn_product_sum += (10 * 1 if isbn[-1] == 'X' else int(isbn[-1]) * 1 )
    for multiple, char in enumerate(isbn[-2::-1], start=2):
        if char.isdigit():
            isbn_product_sum += int(char) * multiple
        else:
            return False
    return not isbn_product_sum % 11