"""Module implementing a Caesar cipher rotation function."""

def rotate(text, key):
    """Return the rotated (Caesar cipher) version of the input text."""
    result = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            rotated = (ord(char) - base + key) % 26 + base
            result += chr(rotated)
        else:
            result += char

    return result