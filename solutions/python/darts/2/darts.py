"""Dart scoring module."""

def score(x_coordinate, y_coordinate):
    """Calculate score based on distance from origin."""
    distance = (x_coordinate ** 2 + y_coordinate ** 2) ** 0.5

    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0