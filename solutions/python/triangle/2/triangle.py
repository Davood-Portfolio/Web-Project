"""Module for classifying triangles."""


def is_valid_triangle(sides):
    smallest_side, middle_side, largest_side = sorted(sides)
    return smallest_side > 0 and smallest_side + middle_side >= largest_side


def equilateral(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    return is_valid_triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 3