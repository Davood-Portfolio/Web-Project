"""Module providing a function to check if a string is an isogram."""

def is_isogram(string):
    """Return True if the string is an isogram, False otherwise."""
    seen = set()
    for char in string.lower():
        if char.isalpha():
            if char in seen:
                return False
            seen.add(char)
    return True