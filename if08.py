def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    
    if a>0 and a%2==0  and a>9 and a<100:
        return 'ikki xonali jufat raqam'
    if a>0 and a%2==1  and a>9 and a<100:
        return 'ikki xonali toq raqam'
    if a>0 and a%2==0  and a>99 and a<1000:
        return 'uch xonali jufat raqam'
    if a>0 and a%2==1  and a>99 and a<1000:
        return 'uch xonali toq raqam'
    
print(main(28))