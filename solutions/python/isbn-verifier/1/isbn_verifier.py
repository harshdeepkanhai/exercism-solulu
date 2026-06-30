def is_valid(isbn):
    isbn = isbn.replace('-',"")
    isbn_product_sum = 0
    
    if len(isbn) != 10:
        return False
    for multiple, char in enumerate(isbn[::-1], start=1):
        if char == "X" and multiple == 1:
            isbn_product_sum += 10 * multiple
        elif char.isdigit():
            isbn_product_sum += int(char) * multiple
        else:
            return False
    return not isbn_product_sum % 11