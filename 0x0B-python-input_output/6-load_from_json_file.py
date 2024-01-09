#!/usr/bin/python3
"""Module: json_file_loader
Creates an object from a "JSON file"
"""

import json

def load_from_json_file(filename):
    """Creates an object from a "JSON file".

    Args:
        filename (str): The name of the file to create an object from.
    
    Returns:
        object: The Python object created from the JSON representation in the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

