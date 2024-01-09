#!/usr/bin/python3
"""Module: json_object_converter
Returns the dictionary description of an object as a simple data structure for JSON.
"""

def class_to_json(obj):
    """Returns the dictionary description of an object as a simple data structure for JSON.

    Args:
        obj: The object to be converted.

    Returns:
        dict: A dictionary representing the object's attributes.
    """
    return obj.__dict__

