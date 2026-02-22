"""
Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """Calculate preparation time.

    :param layers: int - number of layers added to the lasagna.
    :return: int - total preparation time (in minutes).
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate total elapsed cooking time.

    :param layers: int - number of layers added.
    :param elapsed_bake_time: int - time already spent baking.
    :return: int - total time spent (prep + baking).
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
