def to_rna(dna_strand: str) -> str:
    translation_map = str.maketrans({'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'})
    return dna_strand.translate(translation_map)
