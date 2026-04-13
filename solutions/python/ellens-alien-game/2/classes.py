"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with coordinates and health."""

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int):
        """Initialize alien with position and default health."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Reduce health by 1."""
        self.health -= 1

    def is_alive(self) -> bool:
        """Return True if alien is alive."""
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        """Move alien to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other: "Alien"):
        """Collision detection not implemented."""
        pass


def new_aliens_collection(coordinates):
    """Create a list of Alien objects from coordinate pairs."""
    return [
        Alien(x_coordinate, y_coordinate)
        for x_coordinate, y_coordinate in coordinates
    ]