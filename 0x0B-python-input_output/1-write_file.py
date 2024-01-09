#!/usr/bin/python3
def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns the number of characters written.

    Args:
        filename (str): The path to the file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters_written = file.write(text)

    return num_characters_written

