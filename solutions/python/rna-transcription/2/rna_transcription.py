def to_rna(dna_strand: str) -> str:
    translation_map = str.maketrans('GCTA', 'CGAU')
    return dna_strand.translate(translation_map)
