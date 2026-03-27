def get_rounds(number):
    """Create a list containing the current and next two round numbers."""
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers."""
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""
    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list."""
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Check if approximate averages equal the true average."""
    true_avg = card_average(hand)

    first_last_avg = (hand[0] + hand[-1]) / 2

    mid_index = len(hand) // 2
    if len(hand) % 2 == 0:
        middle_avg = (hand[mid_index - 1] + hand[mid_index]) / 2
    else:
        middle_avg = hand[mid_index]

    return first_last_avg == true_avg or middle_avg == true_avg


def average_even_is_average_odd(hand):
    """Check if average of even indices equals average of odd indices."""
    even_cards = hand[::2]
    odd_cards = hand[1::2]

    return (sum(even_cards) / len(even_cards)) == (sum(odd_cards) / len(odd_cards))


def maybe_double_last(hand):
    """Multiply last card by 2 if it is a Jack (11)."""
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand