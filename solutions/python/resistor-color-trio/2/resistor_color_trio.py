"""Module for converting resistor color bands into human‑readable labels."""

def label(colors):
    """Return the resistor value (with metric prefix) based on three color bands."""
    color_values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    first_color, second_color, multiplier_color = colors[:3]

    base_value = color_values[first_color] * 10 + color_values[second_color]
    resistance = base_value * (10 ** color_values[multiplier_color])

    if resistance >= 1_000_000_000:
        return f"{resistance // 1_000_000_000} gigaohms"
    if resistance >= 1_000_000:
        return f"{resistance // 1_000_000} megaohms"
    if resistance >= 1_000:
        return f"{resistance // 1_000} kiloohms"

    return f"{resistance} ohms"
