def write_file(filename="", text=""):
    """function that writes a string and returns the number"""

    with open(filename, 'w', encoding='utf-8') as f:
        chars_written = f.write(text)
        return chars_written
