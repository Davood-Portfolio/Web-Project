"""Functions to help play and score a game of blackjack."""


def value_of_card(card):
    """Return the integer value of a card."""
    if card in ("J", "Q", "K"):
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Return the card with the higher value, or both if equal."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Return 11 if it doesn't bust, otherwise 1."""
    value_one = 11 if card_one == "A" else value_of_card(card_one)
    value_two = 11 if card_two == "A" else value_of_card(card_two)

    total = value_one + value_two

    if total + 11 <= 21:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Check if the hand is a natural blackjack."""
    cards = {card_one, card_two}
    return "A" in cards and any(card in ("10", "J", "Q", "K") for card in cards)


def can_split_pairs(card_one, card_two):
    """Check if cards have equal value."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Check if total is 9, 10, or 11."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return 9 <= total <= 11