"""Number classification module."""

def classify(number):
    """Classify a number as perfect, abundant, or deficient."""
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisor_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == number:
        return "perfect"
    if divisor_sum > number:
        return "abundant"
    return "deficient"