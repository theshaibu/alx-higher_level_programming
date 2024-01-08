#!/usr/bin/python3
"""
Module text_indentation
Prints a text with two newlines
Adds two newlines after each of these characters: '.', '?', ':'.
"""

def text_indentation(text):
    """
    Prints a text and adds two newlines
    after each of these characters: '.', '?', ':'.
    
    Parameters:
    - text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

