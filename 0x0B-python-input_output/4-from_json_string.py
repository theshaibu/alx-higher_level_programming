#!/usr/bin/python3
"""Module: json_parser
Returns an object (Python data structure) represented by a JSON string
"""

import json

def from_json_string(my_str):
    """Returns an object represented by a JSON string (Python data structure)

    Args:
        my_str (str): The JSON string to be deserialized.
    
    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

