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

    # 1-band resistor
    if len(colors) == 1:
        return "0 ohms"

    # 4-band resistor
    if len(colors) == 4:
        d1, d2, multiplier_color, tolerance_color = colors
        base_value = digit_values[d1] * 10 + digit_values[d2]
        multiplier = 10 ** digit_values[multiplier_color]
        tolerance = tolerance_values[tolerance_color]

    # 5-band resistor
    elif len(colors) == 5:
        d1, d2, d3, multiplier_color, tolerance_color = colors
        base_value = (
            digit_values[d1] * 100 +
            digit_values[d2] * 10 +
            digit_values[d3]
        )
        multiplier = 10 ** digit_values[multiplier_color]
        tolerance = tolerance_values[tolerance_color]

    else:
        raise ValueError("Invalid number of color bands")

    resistance = base_value * multiplier

    # Determine unit with float division
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
    if value.is_integer():
        value = int(value)

    return f"{value} {unit} {tolerance}"
