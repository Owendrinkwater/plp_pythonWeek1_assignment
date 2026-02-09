def divisible_by_ten(num):
    """The function should return True if 
    num is divisible by 10, and False otherwise.

    Args:
        num (int): number to be checked

    Returns:
        boolean: true if num is divisible by 10, false otherwise
    """
    if num % 10 == 0:
        return True
    else:
        return False
    
print(divisible_by_ten(50))   
print(divisible_by_ten(33))   
print(divisible_by_ten(0))    

