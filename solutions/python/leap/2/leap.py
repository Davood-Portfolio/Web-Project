"""Module for checking leap years."""


def leap_year(year):
    """Return True if the given year is a leap year, otherwise False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)