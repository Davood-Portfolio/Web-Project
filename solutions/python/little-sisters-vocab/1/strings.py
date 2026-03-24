"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = [prefix] + [prefix + word for word in vocab_words[1:]]
    return " :: ".join(words)


def remove_suffix_ness(word):
    base = word[:-4]
    if base.endswith("i"):
        return base[:-1] + "y"
    return base


def adjective_to_verb(sentence, index):
    words = sentence.split()
    word = words[index].strip(".,!?")
    return word + "en"