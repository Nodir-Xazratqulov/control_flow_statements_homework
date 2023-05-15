def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    x = 0
    if a<0:
        x += 1
    if b<0:
        x += 1
    if c<0:
        x += 1

    return x
    
print(main(1,-2,3))