def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp<0:
        return 'muzlamoqda'
    if 1<temp and temp<10:
        return 'juda sovuq'
    if 11<temp and temp<22:
        return 'sovuq'
    if 21<temp and temp<30:
        return 'oddiy'
    if 31<temp and temp<40:
        return 'issiq'
    if temp>40:
        return 'juda issiq'
    
print(main(16))