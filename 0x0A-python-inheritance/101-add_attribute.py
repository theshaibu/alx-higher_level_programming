#!/usr/bin/python3
def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
    - obj: The object to which the attribute will be added.
    - attr_name: The name of the new attribute.
    - attr_value: The value of the new attribute.

    Raises:
    - TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")

