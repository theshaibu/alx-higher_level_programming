#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: The object to inspect.

    Returns:
    - A list of attribute and method names.
    """
    return dir(obj)

# Example usage:
my_list = [1, 2, 3]
result = lookup(my_list)
print(result)

