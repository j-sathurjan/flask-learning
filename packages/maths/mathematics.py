"""this module give functions to add, subtract and multiply two values.
"""
def summation(a, b):
    """this function takes two number a and b then return sum of them.

    Args:
        a (float): take float number as input
        b (float): take float number as input
    """
    try:
        result = float(a) + float(b)
    except Exception:
        result = "invalid input"
    return result

def subtraction(a, b):
    """this function takes two number a and b then return a-b.

    Args:
        a (float): take float number as input
        b (float): take float number as input
    """
    try:
        result = float(a) - float(b)
    except Exception:
        result = "invalid input"
    return result

def multiplication(a, b):
    """this function takes two number a and b then return a*b.

    Args:
        a (float): take float number as input
        b (float): take float number as input
    """
    try:
        result = float(a) * float(b)
    except Exception:
        result = "invalid input"
    return result
