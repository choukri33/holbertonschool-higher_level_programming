#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8) and
    returns the number of characters written"""


def write_file(filename="", text=""):
    """
    Writes the input text to a file specified by the filename.
    
    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.
        
    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        """Write string and count characters"""

        chars_written = f.write(text)
        return len(text)
