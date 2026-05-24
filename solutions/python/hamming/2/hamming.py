"""Module for computing distance between two strands."""


def distance(strand_a, strand_b):
    """Calculate the distance between two strands.

    Raises:
        ValueError: If strands are not of equal length.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    mismatch_count = 0

    for base_a, base_b in zip(strand_a, strand_b):
        if base_a != base_b:
            mismatch_count += 1

    return mismatch_count