"""House that Jack Built recitation module."""

PHRASES = [
    ("the house that Jack built.", ""),
    ("the malt", "that lay in "),
    ("the rat", "that ate "),
    ("the cat", "that killed "),
    ("the dog", "that worried "),
    ("the cow with the crumpled horn", "that tossed "),
    ("the maiden all forlorn", "that milked "),
    ("the man all tattered and torn", "that kissed "),
    ("the priest all shaven and shorn", "that married "),
    ("the rooster that crowed in the morn", "that woke "),
    ("the farmer sowing his corn", "that kept "),
    ("the horse and the hound and the horn", "that belonged to "),
]


def recite(start_verse, end_verse):
    """Return verses from start_verse to end_verse as a list of strings."""
    verses = []

    for verse_index in range(start_verse - 1, end_verse):
        verse_parts = ["This is " + PHRASES[verse_index][0]]

        for phrase_index in range(verse_index, 0, -1):
            connector = PHRASES[phrase_index][1]
            previous_phrase = PHRASES[phrase_index - 1][0]
            verse_parts.append(connector + previous_phrase)

        full_verse = " ".join(verse_parts)
        verses.append(full_verse)

    return verses