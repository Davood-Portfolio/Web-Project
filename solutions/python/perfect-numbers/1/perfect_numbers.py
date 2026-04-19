def classify(number):
    """A perfect number equals the sum of its positive divisors."""
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    if divisor_sum == number:
        return "perfect"
    if divisor_sum > number:
        return "abundant"
    return "deficient"