def validator(t: str = None, u: str = None) -> bool:
    """Validates a solution to the RNA transcription problem."""
    # First, check input types and format
    if t is None or u is None:
        print("Input DNA string or RNA string is None")
        return False
    if not isinstance(t, str) or not isinstance(u, str):
        print("Both inputs must be strings")
        return False

    # Check if strings are empty
    if not t or not u:
        print("Input strings cannot be empty")
        return False

    # Check DNA string contains only A, C, G, T
    for letter in t:
        if letter not in "ACGT":
            print(f"DNA string contains invalid character: {letter}")
            return False

    # Check RNA string contains only A, C, G, U
    for letter in u:
        if letter not in "ACGU":
            print(f"RNA string contains invalid character: {letter}")
            return False

    # Check if lengths match
    if len(t) != len(u):
        print(f"Length mismatch: DNA has {len(t)} characters, RNA has {len(u)} characters")
        return False

    # Comment
    # Padding
    # To prevent seeing solution
    # in case they hit an error

    # Check if transcription is correct
    # Compare each position - should match except T->U
    for i, (dna_base, rna_base) in enumerate(zip(t, u)):
        if dna_base == 'T':
            if rna_base != 'U':
                print(f"Transcription error at position {i}: expected 'U' for 'T', got '{rna_base}'")
                return False
        else:
            if dna_base != rna_base:
                print(f"Transcription error at position {i}: '{dna_base}' should remain '{dna_base}', not become '{rna_base}'")
                return False

    return True  # The solution is valid