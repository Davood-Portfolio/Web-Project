"""Functions for organizing and calculating student exam scores."""

from typing import List


def round_scores(student_scores: List[float]) -> List[int]:
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores: List[int]) -> int:
    """Count the number of students with scores <= 40."""
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores: List[int], threshold: int) -> List[int]:
    """Return scores greater than or equal to threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> List[int]:
    """Return grade thresholds for D, C, B, A."""
    passing_score = 40
    interval = (highest - passing_score) // 4

    return [
        passing_score + 1 + step * interval
        for step in range(4)
    ]


def student_ranking(student_scores: List[int], student_names: List[str]) -> List[str]:
    """Return ranking in format '<rank>. <name>: <score>'."""
    return [
        f"{rank}. {name}: {score}"
        for rank, (name, score) in enumerate(
            zip(student_names, student_scores),
            start=1
        )
    ]


def perfect_score(student_info: List[List]) -> List:
    """Return first student with score 100, else empty list."""
    for student_name, score in student_info:
        if score == 100:
            return [student_name, score]
    return []