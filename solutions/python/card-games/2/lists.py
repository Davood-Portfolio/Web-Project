"""Functions for tracking poker hands and performing card-related calculations."""


def get_rounds(number):
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    true_avg = card_average(hand)

    first_last_avg = (hand[0] + hand[-1]) / 2

    mid_index = len(hand) // 2
    if len(hand) % 2 == 0:
        middle_avg = (hand[mid_index - 1] + hand[mid_index]) / 2
    else:
        middle_avg = hand[mid_index]

    return true_avg in (first_last_avg, middle_avg)


def average_even_is_average_odd(hand):
    even_cards = hand[::2]
    odd_cards = hand[1::2]

    return (sum(even_cards) / len(even_cards)) == (sum(odd_cards) / len(odd_cards))


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand