from typing import List


def add_me_to_the_queue(
    express_queue: List[str],
    normal_queue: List[str],
    ticket_type: int,
    person_name: str
) -> List[str]:
    """Add a person to the appropriate queue based on ticket type."""
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue

    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue: List[str], friend_name: str) -> int:
    """Return the index of a friend in the queue."""
    return queue.index(friend_name)


def add_me_with_my_friends(
    queue: List[str],
    index: int,
    person_name: str
) -> List[str]:
    """Insert a person at a specific position in the queue."""
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: List[str], person_name: str) -> List[str]:
    """Remove a person from the queue."""
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: List[str], person_name: str) -> int:
    """Count how many times a name appears in the queue."""
    return queue.count(person_name)


def remove_the_last_person(queue: List[str]) -> str:
    """Remove and return the last person in the queue."""
    return queue.pop()


def sorted_names(queue: List[str]) -> List[str]:
    """Return a new list of names sorted alphabetically."""
    return sorted(queue)