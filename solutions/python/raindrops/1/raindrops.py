"""Module for converting numbers to raindrop sounds."""


def convert(number):
    """Return a string based on raindrop factors."""
    result = ""

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    return result if result else str(number)