"""Utilities for tracking poker rounds and evaluating card hands."""

from typing import List


def get_rounds(number: int) -> List[int]:
    """Return the current round and the next two consecutive rounds."""
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    """Return a concatenated list of two round lists."""
    return rounds_1 + rounds_2


def list_contains_round(rounds: List[int], number: int) -> bool:
    """Return True if the specified round number is in the list."""
    return number in rounds


def card_average(hand: List[int]) -> float:
    """Return the arithmetic mean of the card values in hand."""
    return sum(hand) / len(hand)


def approx_average_is_average(hand: List[int]) -> bool:
    """Check if either approximate average equals the true average."""
    true_avg = card_average(hand)

    first_last_avg = (hand[0] + hand[-1]) / 2

    length = len(hand)
    mid = length // 2

    if length % 2 == 0:
        middle_avg = (hand[mid - 1] + hand[mid]) / 2
    else:
        middle_avg = hand[mid]

    return true_avg in (first_last_avg, middle_avg)


def average_even_is_average_odd(hand: List[int]) -> bool:
    """Return True if averages of even and odd indexed cards are equal."""
    even_cards = hand[::2]
    odd_cards = hand[1::2]

    return (sum(even_cards) / len(even_cards)) == (
        sum(odd_cards) / len(odd_cards)
    )


def maybe_double_last(hand: List[int]) -> List[int]:
    """Double the last card value if it is a Jack (value 11)."""
    jack_value = 11  # fixed: snake_case instead of UPPER_CASE

    if hand[-1] == jack_value:
        hand[-1] *= 2

    return hand