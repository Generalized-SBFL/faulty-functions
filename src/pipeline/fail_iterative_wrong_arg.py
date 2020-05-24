"""Sample file for correct implementation"""

def compute_iterative_factorial(actual_value, value = 24): # fault
    """Assumes value is a natural number
    Returns value!"""
    if value < 0:
        raise ValueError("Inputs of 0 or grater!")
        value = 0
    result = 1
    while value != 0:
        result *= value
        value -= 1
    return result


def compute_recursive_factorial(value):
    """Assumes value is a natural number
    Returns value!"""
    if value < 1:
        return 1
    else:
        return value * compute_recursive_factorial(value - 1)
