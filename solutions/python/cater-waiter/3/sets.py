"""Functions for compiling dishes and ingredients for a catering company."""

from typing import List, Set, Tuple

from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
)


def clean_ingredients(dish_name: str, dish_ingredients: List[str]) -> Tuple[str, Set[str]]:
    """Return dish name and a set of unique ingredients."""
    return dish_name, set(dish_ingredients)


def check_drinks(drink_name: str, drink_ingredients: List[str]) -> str:
    """Return drink name labeled as Cocktail or Mocktail."""
    return (
        f"{drink_name} Cocktail"
        if set(drink_ingredients) & ALCOHOLS
        else f"{drink_name} Mocktail"
    )


def categorize_dish(dish_name: str, dish_ingredients: Set[str]) -> str:
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


def tag_special_ingredients(dish: Tuple[str, List[str]]) -> Tuple[str, Set[str]]:
    """Return dish name and its special ingredients."""
    name, ingredients = dish
    return name, set(ingredients) & SPECIAL_INGREDIENTS


def compile_ingredients(dishes: List[Set[str]]) -> Set[str]:
    """Return a set of all ingredients from all dishes."""
    return set().union(*dishes)


def separate_appetizers(dishes: List[str], appetizers: List[str]) -> List[str]:
    """Return dishes excluding those listed as appetizers."""
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: List[Set[str]], intersection: Set[str]) -> Set[str]:
    """Return ingredients that appear in only one dish."""
    return set().union(*dishes) - intersection