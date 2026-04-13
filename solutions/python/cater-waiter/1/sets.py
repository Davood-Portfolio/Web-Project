"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    if dish_ingredients.issubset(VEGAN):
        category = "VEGAN"
    elif dish_ingredients.issubset(VEGETARIAN):
        category = "VEGETARIAN"
    elif dish_ingredients.issubset(KETO):
        category = "KETO"
    elif dish_ingredients.issubset(PALEO):
        category = "PALEO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    dish_name, ingredients = dish
    special = set(ingredients) & SPECIAL_INGREDIENTS
    return (dish_name, special)


def compile_ingredients(dishes):
    all_ingredients = set()
    for dish in dishes:
        all_ingredients |= dish
    return all_ingredients


def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    all_ingredients = set()

    for dish in dishes:
        all_ingredients |= dish

    return all_ingredients - intersection