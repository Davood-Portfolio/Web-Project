"""Module for checking Armstrong numbers."""


def is_armstrong_number(number):
    digits = [int(digit_char) for digit_char in str(number)]
    power = len(digits)
    return sum(digit_value ** power for digit_value in digits) == number