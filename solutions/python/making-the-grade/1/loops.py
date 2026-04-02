"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count scores less than or equal to 40."""
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    """Return scores greater than or equal to threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Return grade thresholds for D, C, B, A."""
    interval = (highest - 40) // 4
    return [41 + i * interval for i in range(4)]


def student_ranking(student_scores, student_names):
    """Return ranking list with format '<rank>. <name>: <score>'."""
    return [
        f"{rank}. {name}: {score}"
        for rank, (name, score) in enumerate(zip(student_names, student_scores), start=1)
    ]


def perfect_score(student_info):
    """Return first student with score 100, else empty list."""
    for student in student_info:
        if student[1] == 100:
            return student
    return []