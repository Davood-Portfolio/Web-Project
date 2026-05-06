def label(colors):
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

    # Only first 3 colors matter
    c1, c2, c3 = colors[:3]

    main_value = color_values[c1] * 10 + color_values[c2]
    value = main_value * (10 ** color_values[c3])

    if value >= 1_000_000_000:
        return f"{value // 1_000_000_000} gigaohms"
    if value >= 1_000_000:
        return f"{value // 1_000_000} megaohms"
    if value >= 1_000:
        return f"{value // 1_000} kiloohms"
    return f"{value} ohms"
