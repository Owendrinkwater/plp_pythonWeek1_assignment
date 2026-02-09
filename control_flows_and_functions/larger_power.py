def large_power(base, exponent):
    """If base raised to the exponent is greater 
    than 5000, return True, otherwise return False

    Args:
        base(float)
        exponent(float)

    Returns:
        boolean: If base raised to the exponent is greater than 5000, return True, otherwise return False
    """
    result = base ** exponent

    if result > 5000:
        return True
    else:
        return False

print(large_power(10, 3))  
print(large_power(8, 5))   
