#!/usr/bin/python3
"""
Module: 4-inherits_from.py
Checking if the object is an instance from a class int or from a class object
"""

def inherits_from(obj, a_class):
    """Checking if the object is an instance of a class inherited from a class.

    Args:
        obj: The object to check.
        a_class: The class to evaluate.

    Returns:
        True if the object is an instance of a class inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class

