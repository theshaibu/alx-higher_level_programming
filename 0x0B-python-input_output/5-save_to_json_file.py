#!/usr/bin/python3
"""Module: json_file_saver
Writes an object to a text file using a JSON representation
"""

import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj (object): The Python object to be serialized and saved to the file.
        filename (str): The name of the file to which the JSON representation will be written.
    """
    with open(filename, 'w+') as file:
        json.dump(my_obj, file)

