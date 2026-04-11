"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    """Add items to the shopping cart."""
    cart = current_cart.copy()
    for item in items_to_add:
        cart[item] = cart.get(item, 0) + 1
    return cart

def read_notes(notes):
    """Read notes and convert them into a shopping cart dictionary."""
    cart = {}
    for item in notes:
        cart[item] = cart.get(item, 0) + 1
    return cart

def update_recipes(ideas, recipe_updates):
    """Update recipe ideas with new content."""
    updated = ideas.copy()
    for key, value in recipe_updates:
        updated[key] = value
    return updated

def sort_entries(cart):
    """Sort shopping cart entries alphabetically by item name."""
    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    """
    Format the shopping cart for the store with aisle and refrigeration info.
    Items are sorted in reverse alphabetical order.
    """
    result = {}
    for item in sorted(cart.keys(), reverse=True):
        qty = cart[item]
        aisle, refrigerated = aisle_mapping[item]
        result[item] = [qty, aisle, refrigerated]
    return result

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update the store inventory after fulfilling a cart."""
    inventory = store_inventory.copy()
    for item, data in fulfillment_cart.items():
        qty_to_buy = data[0]
        if item in inventory:
            inventory[item][0] -= qty_to_buy
            if inventory[item][0] <= 0:
                inventory[item][0] = "Out of Stock"
    return inventory