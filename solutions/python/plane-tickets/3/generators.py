"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats."""
    seat_letters = ["A", "B", "C", "D"]

    for index in range(number):
        yield seat_letters[index % 4]


def generate_seats(number):
    """Generate seat identifiers for airline seats."""
    current_row = 1
    seats_in_current_row = 0

    for _ in range(number):

        if current_row == 13:
            current_row += 1
            seats_in_current_row = 0

        seat_letter = "ABCD"[seats_in_current_row]
        yield f"{current_row}{seat_letter}"

        seats_in_current_row += 1

        if seats_in_current_row == 4:
            current_row += 1
            seats_in_current_row = 0


def assign_seats(passengers):
    """Assign seats to passengers."""
    seat_generator = generate_seats(len(passengers))

    return {
        passenger_name: next(seat_generator)
        for passenger_name in passengers
    }


def generate_codes(seat_numbers, flight_id):
    """Generate 12 character ticket codes."""
    for seat_number in seat_numbers:
        ticket_code = f"{seat_number}{flight_id}"
        yield ticket_code[:12].ljust(12, "0")