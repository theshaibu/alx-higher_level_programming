def add_integer(a, b=98):
    """
    Add two integers or floats and return the result.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("Parameter 'a' must be an integer or float.")
    if not isinstance(b, (int, float)):
        raise TypeError("Parameter 'b' must be an integer or float.")
    
    # Casting a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    
    return a + b

