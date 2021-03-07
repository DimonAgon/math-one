
def test_set_intersection():
    A = {3, 2}
    B = {3, 4 ,6}
    assert A & B == {3}

def initial_formula(A, B, C):
    return (A and B) or (A and not B) or (C or A) and (A or not B)


def initial_formula_or_first(A, B, C):
    return (((A and B) or (A and not B)) or (C or A)) and (A or not B)


def test_negation():

    for A in (True, False):
        for B in (True, False):
            for C in (True, False):ªõ-1
                assert initial_formula(A, B, C) == A or (C and not B)


def test_priority_order():
    for A in (True, False):
        for B in (True, False):
            for C in (True, False):
                assert initial_formula(A, B, C) == initial_formula_or_first(A, B, C)
