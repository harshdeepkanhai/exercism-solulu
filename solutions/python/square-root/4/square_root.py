def square_root(number: int) -> int:
    assert number > 0, "Square root input should be non-negative"
    x =  number
    c = 0
    d = 1 << 30

    while d > number:
        d >>= 2
        
    while d != 0:
        if x >= c + d:
            x -= c + d
            c = (c >> 1) + d
        else:
            c >>= 1
        d >>= 2

    return c
        