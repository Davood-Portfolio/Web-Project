"""Module for calculating Collatz steps."""


def steps(number):
    """Return the number of steps to reach 1 using the Collatz process."""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step_count = 0
    current_value = number

    while current_value != 1:
        if current_value % 2 == 0:
            current_value //= 2
        else:
            current_value = current_value * 3 + 1
        step_count += 1

    return step_count