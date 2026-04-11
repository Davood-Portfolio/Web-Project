"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    cart = current_cart.copy()
    for item in items_to_add:
        cart[item] = cart.get(item, 0) + 1
    return cart

def read_notes(notes):
    cart = {}
    for item in notes:
        cart[item] = cart.get(item, 0) + 1
    return cart

def update_recipes(ideas, recipe_updates):
    updated = ideas.copy()
    for key, value in recipe_updates:
        updated[key] = value
    return updated

def sort_entries(cart):
    # مرتب‌سازی بر اساس حروف الفبا
    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    result = {}
    # معمولاً در این تمرین، خروجی باید بر اساس حروف الفبا به صورت معکوس مرتب شود
    for item in sorted(cart.keys(), reverse=True):
        qty = cart[item]
        aisle, refrigerated = aisle_mapping[item]
        result[item] = [qty, aisle, refrigerated]
    return result

def update_store_inventory(fulfillment_cart, store_inventory):
    inventory = store_inventory.copy()
    
    for item, data in fulfillment_cart.items():
        qty_to_buy = data[0]
        
        if item in inventory:
            # کسر کردن تعداد درخواستی از موجودی انبار (ایندکس 0)
            inventory[item][0] -= qty_to_buy
            
            # اگر موجودی تمام شد یا منفی شد، مقدار را به Out of Stock تغییر بده
            if inventory[item][0] <= 0:
                inventory[item][0] = "Out of Stock"
                
    return inventory