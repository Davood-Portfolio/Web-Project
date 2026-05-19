"""Binary search implementation to find an item in a sorted list."""


def find(search_list, value):
    """Return index of value in sorted list using binary search.

    Args:
        search_list (list): Sorted list of numbers.
        value (int): Value to search for.

    Returns:
        int: Index of value in list.

    Raises:
        ValueError: If value is not found in the list.
    """
    left = 0
    right = len(search_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = search_list[mid]

        if mid_value == value:
            return mid

        if mid_value < value:
            left = mid + 1
        else:
            right = mid - 1

    raise ValueError("value not in array")