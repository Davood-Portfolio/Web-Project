"""Module for generating Bob's responses."""


def response(hey_bob):
    """Return Bob's response based on the input message."""
    message = hey_bob.strip()

    if message == "":
        return "Fine. Be that way!"

    is_question = message.endswith("?")
    has_letters = any(char.isalpha() for char in message)
    is_yelling = has_letters and message.upper() == message

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"

    if is_yelling:
        return "Whoa, chill out!"

    if is_question:
        return "Sure."

    return "Whatever."