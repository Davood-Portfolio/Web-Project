"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    letters = ["A", "B", "C", "D"]
    for i in range(number):
        yield letters[i % 4]


def generate_seats(number):
    """Generate seat identifiers for airline seats."""
    row = 1
    seats_in_row = 0

    for _ in range(number):
        if row == 13:
            row += 1
            seats_in_row = 0

        yield f"{row}{'ABCD'[seats_in_row]}"

        seats_in_row += 1
        if seats_in_row == 4:
            row += 1
            seats_in_row = 0


def assign_seats(passengers):
    """Assign seats to passengers."""
    seat_gen = generate_seats(len(passengers))
    return {p: next(seat_gen) for p in passengers}


def generate_codes(seat_numbers, flight_id):
    """Generate 12 character ticket codes."""
    for seat in seat_numbers:
        code = f"{seat}{flight_id}"
        yield code[:12].ljust(12, "0")