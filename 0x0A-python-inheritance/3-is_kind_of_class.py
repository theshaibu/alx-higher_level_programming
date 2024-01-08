#!/usr/bin/python3
"""
Module: is_kind_of_class
Check if the object is an instance of, or if the object is an instance of a class that inherited from.

Returns True if it is an instance of a class.
Otherwise, return False
"""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of a_class or a class inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a_class or a class inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class)

