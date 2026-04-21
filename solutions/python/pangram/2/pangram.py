"""Module providing a function to check if a sentence is a pangram."""

def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(sentence.lower()))