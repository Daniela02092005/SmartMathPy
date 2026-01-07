def union(A: set, B: set):
    """
    The “union” function takes two sets as input and returns a new set containing all the elements of both input sets. 
    This is based on the definition:
        Assuming that A and B are sets, the union of A and B, denoted by AUB, is defined as follows: AUB = { x | x∈A v x∈B}
        Therefore, for all x, x∈AUB if and only if x∈A or x∈B.
    """
    result = set()

    for element in A:
        result.add(element)
    
    for element in B:
        if element not in result:
            result.add(element)

    return result


def intersection(A: set, B: set):
    """
    The `intersection` function takes two sets A and B as input and returns the intersection of elements between the two sets, generating a 
    ValueError if there are no common elements, by design. This is based on the following definitions:
        1. If A and B are sets, we define the intersection of A with B, denoted A∩B, as follows: A∩B = {x∈A | x∈B}. We then have that 
        for all x, x∈A∩B if and only if x∈A and x∈B. 

        2. Two sets A and B are called disjoint if they have no elements in common, that is, if their intersection is empty: A∩B=∅
    """

    result = set()

    for element in A:
        if element in B:
            result.add(element)

    if not result:
        raise ValueError("A and B are disjoint")

    return result

def set_difference(A: set, B: set):
    """
    The “set difference” function takes two sets A and B as input and returns the set of elements that are in set A but not in set B. 
    Based on the definition:
        If A and B are sets, the set difference of A and B is defined as A-B, as follows: A-B = {x∈A | x∉B}. Such that x∈A-B if and only 
        if x∈A and x∉B.
    """
    result = set()

    for element in A:
        if element not in B:
            result.add(element)
    
    return result

def symmetric_difference(A: set, B: set):
    """
    The `symmetric_difference` function calculates the symmetric difference between two sets A and B by finding the elements that are only 
    in one of the sets. This is based on the following definition:
        If A and B are sets, their symmetric difference, denoted AΔB, is defined as follows: AΔB = (A-B) U (B-A).
    """
    first_part = set_difference(A, B)
    second_part = set_difference(B, A)
    
    result = union(first_part, second_part)

    return result

def contained(A: set, B: set):
    """
    The function checks whether all elements of set A are also present in set B and returns True if so, False otherwise. 
    This is based on the definition:
        If A and B are sets and every element of A is an element of B, we say that A is contained in B (or that A is a subset of B, or that B 
        contains A, or that B is a superset of A) and we write A ⊆ B. A ⊆ B if and only if, for all x, if x ∈ A, then x ∈ B.
    """
    result = True

    for element in A:
        if element not in B:
            result = False
            break

    return result

def strictly_contained(A: set, B: set):
    """
    The function `strictly_contained` checks whether set A is strictly contained in set B. Based on the definition:
        If A and B are sets with A ⊆ B and A ≠ B, we say that A is strictly contained in B (or that A is a proper subset of B, or that B 
        strictly contains A) and we write A ⊂ B; in symbols: A⊂B if and only if A⊆B and A≠B if and only if A⊆B and there exists such an x 
        that x∈B and x∉A.
        That is, A must be contained in B but they cannot be the same.
    """
    result = contained(A, B)
    if result == True and A != B:
        result = True
    else:
        result = False

    return result

def complement(R: set, A: set):
    """
    The `complement` function takes two sets `R` and `A`, and returns the difference between `R` and `A`, based on the definition:
        Suppose we have a reference set R and that A⊆R. The set R-A is called the complement of A with respect to R and is denoted Cr(A) or 
        simply C(A), if there is no risk of confusion. We thus have that: x∈Cr(A) if and only if x∈R and x∉A.
    """
    result = set_difference(R, A)
    return result

def power_set(A: set):
    """
    The function creates the power set of a given set A, based on axiom 6 of the set of parts:
        If A is any set, there exists a set whose elements are precisely all the subsets of A; this set is called the set of parts of A 
        (or power set of A) and we denote it P(A).
        Thus, if A is a set, x∈P(A) if and only if x⊆A.
    """
    empty = tuple()

    power_set = set()
    power_set.add(empty)

    for element in A:
        copy = power_set.copy()
        for subset in copy:
            subset_copy = list(subset)
            subset_copy.append(element)
            new_subset = tuple(subset_copy)
            power_set.add(new_subset)

    return power_set

def cartesian_product(A: set, B: set):
    """
    The `cartesian_product` function takes two sets as input and returns the Cartesian product of the two sets as a set of tuples. 
    This is based on the definition:
        If A and B are arbitrary sets, we know that the Cartesian product of A and B is the set given by: 
        AxB = {(x,y)|x∈A ∧ y∈B}, which is not commutative.
        We therefore have that (x,y)∈AxB if and only if x∈A and y∈B.
    """
    result = set()

    for elementA in A:
        for elementB in B:
            a = elementA
            b = elementB
            orderly_pair = (a,b)
            result.add(orderly_pair)

    return result