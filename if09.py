def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    
    x = int(a%10)
    y = int(a//10)
    z = int(x*10+y)

    if z>a:
        return True
    if z<a:
        return False
    
print(main(31))