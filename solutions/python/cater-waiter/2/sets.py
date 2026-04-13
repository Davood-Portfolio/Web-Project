"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Return dish name and a set of unique ingredients."""
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Return drink name labeled as Cocktail or Mocktail."""
    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Return dish name with its dietary category."""
    if dish_ingredients.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    if dish_ingredients.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    if dish_ingredients.issubset(KETO):
        return f"{dish_name}: KETO"
    if dish_ingredients.issubset(PALEO):
        return f"{dish_name}: PALEO"
    return f"{dish_name}: OMNIVORE"


def tag_special_ingredients(dish):
    """Return dish name and its special ingredients."""
    dish_name, ingredients = dish
    return (dish_name, set(ingredients) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes):
    """Return a set of all ingredients from all dishes."""
    all_ingredients = set()
    for dish in dishes:
        all_ingredients |= dish
    return all_ingredients


def separate_appetizers(dishes, appetizers):
    """Return dishes excluding those listed as appetizers."""
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    """Return ingredients that appear in only one dish."""
    all_ingredients = set()
    for dish in dishes:
        all_ingredients |= dish
    return all_ingredients - intersection