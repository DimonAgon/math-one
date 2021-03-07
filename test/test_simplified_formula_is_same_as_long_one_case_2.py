


def set_difference(X, Y):
    """# True \ False = True
# True \ True = False
# False \ True = False
# False \ False = False
That is z must be in  X and must not be in Y
"""
    return X and not Y


def initial_formula(A, B, C):
    return A and set_difference(A, set_difference(A, B)) or C


def test_initial_formula_is_equal_to_simplified():
    for A in (True, False):
        for B in (True, False):
            for C in (True, False):
                assert initial_formula(A, B, C) == (A and B or C)
