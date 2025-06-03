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
    if invalid := (set(t) - set("ACGT")):
        print(f"DNA string contains invalid character(s): {invalid}")
        return False

    # Check RNA string contains only A, C, G, U
    if invalid := (set(u) - set("ACGU")):
        print(f"RNA string contains invalid character(s): {invalid}")
        return False

    # Check if lengths match
    if len(t) != len(u):
        print(
            "Length mismatch: "
            + f"DNA has {len(t)} characters, RNA has {len(u)} characters"
        )
        return False

    # Comment
    # Padding
    # To prevent seeing solution
    # in case they hit an error

    # Check if transcription is correct
    # Compare each position - should match except T->U
    for i, (dna_base, rna_base) in enumerate(zip(t, u)):
        position_err = f"Transcription error at position {i}: "
        if dna_base == "T" and rna_base != "U":
            print(position_err + f"expected 'U' for 'T', got '{rna_base}'")
            return False
        elif dna_base != "T" and dna_base != rna_base:
            print(
                position_err
                + f"'{dna_base}' should be the same, not become '{rna_base}'"
            )
            return False

    return True  # The solution is valid
