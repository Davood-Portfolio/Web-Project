"""Module for converting a DNA strand to its RNA complement."""


def to_rna(dna_strand):
    """Return the RNA complement of a DNA strand."""
    mapping = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }

    return "".join(mapping[nucleotide] for nucleotide in dna_strand)