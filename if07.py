def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2==0:
        return 'musbat juft'
    if a>0 and a%2==1:
        return 'musbat toq'
    if a<0 and a%2==0:
        return 'manfiy juft'
    if a<0 and a%2==1:
        return 'manfiy toq'
    
print(main(-10))