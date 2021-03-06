



def compute_simplified_formula(A, B, C):
    b_diff_c = B - C
    a_intersect_b_diff_c = A & b_diff_c
    return a_intersect_b_diff_c

def set_difference(X, Y):
    """# True \ False = True
# True \ True = False
# False \ True = False
# False \ False = False
That is z must be in  X and must not be in Y
"""
    return X and not Y


def initial_formula(A, B, C):
    return not C and set_difference(A, C) and set_difference(B, C) and (not C or B)


def test_initial_formula_is_equal_to_simplified():
    for A in (True, False):
        for B in (True, False):
            for C in (True, False):
                assert initial_formula(A, B, C) == (A and set_difference(B, C))