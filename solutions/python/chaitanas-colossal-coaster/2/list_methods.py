"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add person to the correct queue based on ticket type."""
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue

    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue, friend_name):
    """Return index of friend in queue."""
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    """Insert person at a given index."""
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Remove a specific person from queue."""
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    """Count occurrences of a name in queue."""
    return queue.count(person_name)


def remove_the_last_person(queue):
    """Remove and return last person in queue."""
    return queue.pop()


def sorted_names(queue):
    """Return a sorted copy of the queue."""
    return sorted(queue)