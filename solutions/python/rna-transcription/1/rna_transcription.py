def to_rna(dna_strand):
    mapping = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    
    rna = ""
    
    for nucleotide in dna_strand:
        rna += mapping[nucleotide]
    
    return rna