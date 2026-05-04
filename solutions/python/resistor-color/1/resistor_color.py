"""Module for working with resistor color codes."""

COLOR_CODES = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def color_code(color):
    """Return the numerical code for a given color."""
    return COLOR_CODES.index(color)


def colors():
    """Return the list of all available colors."""
    return COLOR_CODES