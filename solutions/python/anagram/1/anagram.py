"""Anagram finder module."""

def find_anagrams(word, candidates):
    """Return a list of anagrams of 'word' from 'candidates'."""
    result = []
    normalized_word = word.lower()
    sorted_word = sorted(normalized_word)

    for candidate in candidates:
        normalized_candidate = candidate.lower()

        if normalized_candidate == normalized_word:
            continue

        if sorted(normalized_candidate) == sorted_word:
            result.append(candidate)

    return result