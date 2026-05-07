"""Module for converting resistor color bands into human‑readable labels."""

def resistor_label(colors):
    """Return the resistor value with correct unit and tolerance."""

    digit_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }

    tolerance_values = {
        "grey": "±0.05%",
        "violet": "±0.1%",
        "blue": "±0.25%",
        "green": "±0.5%",
        "brown": "±1%",
        "red": "±2%",
        "gold": "±5%",
        "silver": "±10%"
    }

    # One‑band resistor
    if len(colors) == 1:
        return "0 ohms"

    # Four‑band resistor
    if len(colors) == 4:
        first_digit_color, second_digit_color, multiplier_color, tolerance_color = colors
        base_value = (
            digit_values[first_digit_color] * 10 +
            digit_values[second_digit_color]
        )
        multiplier = 10 ** digit_values[multiplier_color]
        tolerance = tolerance_values[tolerance_color]

    # Five‑band resistor
    elif len(colors) == 5:
        first_digit_color, second_digit_color, third_digit_color, multiplier_color, tolerance_color = colors
        base_value = (
            digit_values[first_digit_color] * 100 +
            digit_values[second_digit_color] * 10 +
            digit_values[third_digit_color]
        )
        multiplier = 10 ** digit_values[multiplier_color]
        tolerance = tolerance_values[tolerance_color]

    else:
        raise ValueError("Invalid number of color bands")

    resistance = base_value * multiplier

    # Determine unit with float precision
    if resistance >= 1_000_000_000:
        value = resistance / 1_000_000_000
        unit = "gigaohms"
    elif resistance >= 1_000_000:
        value = resistance / 1_000_000
        unit = "megaohms"
    elif resistance >= 1000:
        value = resistance / 1000
        unit = "kiloohms"
    else:
        value = resistance
        unit = "ohms"

    # Remove trailing .0 if integer
    if isinstance(value, float) and value.is_integer():
        value = int(value)

    return f"{value} {unit} {tolerance}"
