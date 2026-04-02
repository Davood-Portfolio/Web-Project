"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return the coordinate value from a tuple (treasure, coordinate)."""
    return record[1]


def convert_coordinate(coordinate):
    """Split a string coordinate into a tuple of its components."""
    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    """Compare two records and determine if their coordinates match."""
    azara_coordinate = convert_coordinate(get_coordinate(azara_record))
    rui_coordinate = rui_record[1]
    return azara_coordinate == rui_coordinate


def create_record(azara_record, rui_record):
    """Combine the two records if coordinates match; otherwise return 'not a match'."""
    if not compare_records(azara_record, rui_record):
        return "not a match"

    treasure, coordinate = azara_record
    location, rui_coordinate, quadrant = rui_record

    return (treasure, coordinate, location, rui_coordinate, quadrant)


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records."""
    lines = []

    for record in combined_record_group:
        treasure = record[0]
        location = record[2]
        rui_coordinate = record[3]
        quadrant = record[4]

        cleaned_tuple = (treasure, location, rui_coordinate, quadrant)
        lines.append(str(cleaned_tuple))

    return "\n".join(lines) + "\n"