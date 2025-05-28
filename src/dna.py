def validator(s: str = None, ret: str = None) -> bool:
    """Validates a solution to the DNA problem."""
    # First, check input types and format
    if s is None or ret is None:
        print("Input string or answer value is None")
        return False
    if not isinstance(s, str) or not isinstance(ret, str):
        return False
    ret_split = ret.split()
    for value in ret_split:  # Check if ret is a space-separated string of int
        if not value.isdigit():
            print(f"Expected space-separated integers, got: {value}")
            return False
    if len(ret_split) != 4:  # Check number of provided integers
        print(f"Expected 4 space-separated integers, got: {ret}")
        return False
    for letter in "ACGT":  # Check string contains only A, C, G, T
        if letter not in s:
            print(f"Input missing expected letter {letter}: {s}")
            return False
    str_removed = s.strip().translate(str.maketrans("", "", "ACGT"))
    if str_removed:  # If any characters other than A, C, G, T are present
        print(f"Input string contains invalid characters: {str_removed}")
        return False

    # Comment
    # Padding
    # To prevent seeing solution
    # in case they hit an error

    # make a dictionary from the answer string
    ret_counts = dict(zip("ACGT", map(int, ret.split())))
    # count occurrences of A, C, G, T in the input string
    # using a dictionary comprehension, making a dict within an iteration
    my_counts = {letter: s.count(letter) for letter in "ACGT"}
    # Check if the counts match for each letter
    for letter in "ACGT":  # Only print the mismatch if they differ
        if my_counts[letter] != ret_counts[letter]:
            print(f"Counts do not match for {letter}")
            return False

    return True  # The solution is valid
