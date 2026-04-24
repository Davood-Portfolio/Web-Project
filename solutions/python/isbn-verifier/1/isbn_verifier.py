"""Module providing a function to validate ISBN-10 numbers."""

def is_valid(isbn):
    """Return True if the string is a valid ISBN-10, False otherwise."""
    digits = []
    for char in isbn:
        if char.isdigit():
            digits.append(int(char))
        elif char == 'X' and len(digits) == 9:
            digits.append(10)
        elif char != '-':
            return False

    if len(digits) != 10:
        return False

    total = sum((10 - i) * num for i, num in enumerate(digits))
    return total % 11 == 0