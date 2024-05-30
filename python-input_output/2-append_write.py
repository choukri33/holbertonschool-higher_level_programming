def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        # Append string and count characters
        chars_added = f.write(text)
        return chars_added
