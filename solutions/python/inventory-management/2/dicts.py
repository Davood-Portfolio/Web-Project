"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dictionary with item counts from a list."""
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def add_items(inventory, items):
    """Add items to the inventory or increase their count."""
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory, items):
    """Decrease item counts without letting them go below zero."""
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove an item completely from the inventory."""
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    """Return a list of (item, count) pairs where count is greater than zero."""
    result = []
    for key, value in inventory.items():
        if value > 0:
            result.append((key, value))
    return result