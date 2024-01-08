#!/usr/bin/python3
"""
Module say_my_name
Prints out first name and last name
"""

def say_my_name(first_name, last_name=""):
    """
    Prints out first name and last name.
    
    Parameters:
    - first_name (str): The first name.
    - last_name (str): The last name. Defaults to an empty string.

    Raises:
    TypeError: If either first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))

