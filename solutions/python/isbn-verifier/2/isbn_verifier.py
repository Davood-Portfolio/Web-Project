"""Module providing a function to validate ISBN-10 numbers."""

def is_valid(isbn):
    """Return True if the string is a valid ISBN-10, False otherwise."""
    digits = []
    for character in isbn:
        if character.isdigit():
            digits.append(int(character))
        elif character == 'X' and len(digits) == 9:
            digits.append(10)
        elif character != '-':
            return False

    if len(digits) != 10:
        return False

    total = sum((10 - index) * value for index, value in enumerate(digits))
    return total % 11 == 0