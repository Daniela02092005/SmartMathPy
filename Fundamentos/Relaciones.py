from Conjuntos import cartesian_product, contained, intersection

def diagonal(A: set):
    """
    The `diagonal` function takes a set as input and returns a set of tuples in which each tuple contains an element of the input set repeated
    twice. This is based on:
        Let A be any set. The diagonal relation in A, denoted ∆A, is given by: ∆A = {(x,x)|x∈A}.
    """
    result = set()

    for a in A:
        ordered_pair = (a, a)
        result.add(ordered_pair)

    return result

def composition(A: set, B: set, C: set):
    """
    The `composition` function takes three sets A, B, and C, calculates the Cartesian products of A and B, and B and C, and then finds pairs 
    of elements where the second element of the first pair matches the first element of the second pair, returning a set of resulting pairs. 
    This is based on:
        S relation from A to B, T relation from B to C. We can form the composite of T with S, denoted ToS, and given by: 
        ToS = {(w,x)∈AxC | (∃y∈B)((w,y)∈S ∧ (y,x)∈T)}.
    """
    S = cartesian_product(A, B)
    T = cartesian_product(B, C)
    result = set()

    for s in S:
        DomS = s[0]
        RanS = s[1]
        for t in T:
            DomT = t[0]
            RanT = t[1]
            if RanS == DomT:
                ordered_pair = (DomS, RanT)
                result.add(ordered_pair)
    
    return result

def inverse(A: set, B: set):
    """
    The function inverse takes two sets A and B, computes the Cartesian product of A and B, and returns
    a new set with the pairs reversed.
    """
    original = cartesian_product(A, B)
    result = set()

    for pair in original:
        new_pair = (pair[1], pair[0])
        result.add(new_pair)
    
    return result

def inverse_relation(R: set):
    """
    The function `inverse_relation` takes a set representing a relation and returns its inverse
    relation.
    """
    result = set()

    for a, b in R:
        inverse = (b,a)
        result.add(inverse)

    return result

def reflexive(A: set, R: set):
    """
    The function checks whether a relation R is reflexive based on the elements of the diagonal set. This is based on  Theorem 41, clause a:
        If R is a relation in A, then: R is reflexive if and only if ∆A ⊆ R.
    """
    Diagonal = diagonal(A)

    if contained(Diagonal, R):
        return True
    else:
        return False
    
def symmetric(R: set):
    """
    The `symmetric` function checks whether two sets are equal and returns True if they are, otherwise it returns False. 
    This is based on Theorem 41, clause b:
        If R is a relation on A, then: R is symmetric if and only if R^-1 = R.
    """
    Inverse = inverse_relation(R)

    if Inverse == R:
        return True
    else:
        return False
    
def transitive(R: set):
    """
    The `transitive` function checks whether a set R contains the composition. This is based on Theorem 41, subsection c:
        If R is a relation in A, then: R is transitive if and only if RoR⊆R.
    """
    composition = set()
    for (a, b) in R:
        for (c, d) in R:
            if b == c:
                ordered_pair = (a, d)
                composition.add(ordered_pair)

    if contained(composition, R):
        return True
    else:
        return False
    
def antisymmetric(R: set, A: set):
    """
    The `antisymmetric` function checks whether a relation R is antisymmetric given a set A. This is based on Theorem 41, clause d:
        If R is a relation in A, then: R is antisymmetric if and only if R ∩ R^-1 ⊆ ∆A.
    """
    
    Inverse = inverse_relation(R)
    a = intersection(R, Inverse)
    Diagonal = diagonal(A)

    if contained(a, Diagonal):
        return True
    else:
        return False
    
def equivalence(A: set, R: set):
    """
    The equivalence function checks whether a relation R in set A is reflexive, symmetric, and transitive. This is based on the definition:
        An equivalence relation in a set is a relation that satisfies three fundamental properties: reflexivity, symmetry, and transitivity.
    """
    if reflexive(A, R) and symmetric(R) and transitive(R):
        return True
    else: 
        return False
    
def class_equivalence(R: set, A: set, x):
    """
    The function `equivalence_class` takes a relation R, a set A, and an element x, and returns a set of elements of A that are related to x 
    in R. This is based on the definition:
        Let R be an equivalence relation on A; for all x∈A we define the (equivalence) class of x (according to R), denoted [X]s, or simply 
        [X] if there is no risk of confusion, as the set of all elements of A that are equivalent to x; in symbols: [X]={y∈A|x∼y}.
    """
    result = set()

    for element in A:
        if (x, element) in R:
            result.add(element)
    
    return result
    
def relation_of_order(R: set, A: set):
    """
    The relation_of_order function checks whether a relation R in set A is reflexive, antisymmetric, and transitive. This is based on the 
    definition:
        A relation of order is a binary relation on a set that simultaneously satisfies the properties of reflexivity, antisymmetry, 
        and transitivity.
    """
    if reflexive(A, R) and antisymmetric(R, A) and transitive(R):
        return True
    else: 
        return False
    
def comparable(P: set, a, b):
    """
    The `comparable` function determines whether two elements are comparable based on a given set of pairs. This is based on the definition:
        Let (A, ≤) be a partially ordered set; we say that two elements a and b of A are comparable according to ≤ if a≤b or b≤a; otherwise, 
        a and b are said to be incomparable according to ≤.
    """
        
    if (a, b) in P or (b, a) in P:
        return "Comparable"
    else:
        return "Incomparable"
    
def total_order(P: set, A: set):
    """
    The `total_order` function checks whether a given set of pairs satisfies the total order property. This is based on the definition:
        A partially ordered set (A, ≤) is called a total order (or linear order or chain) if there are no elements in A that are incomparable
        according to ≤; in other words, if every pair of elements in A is comparable according to ≤.
    """

    result = True

    for a in A:
        for b in A:
            if (a, b) in P or (b, a) in P:
                continue
            else:
                result = False
                break

    return result

def minmax(P: set, A: set):
    """
    The minmax function takes two sets P and A as input and returns the minimum and maximum elements of set A based on the relation defined 
    in set P. Starting from the definition:
        Let (A, ≤) be a partially ordered set:
        1. An element m∈A is a minimal element in A if, for all x∈A, having x≤m implies x=m (that is, m is a minimal element in A if m∈A and 
        there are no elements in A that strictly precede m).
        2. An element n∈A is maximal in A if, for all x∈A, having n≤x implies n=x (that is, n is maximal in A if n∈A and there are no 
        elements in A that strictly follow n).

        In this implementation, we restrict ourselves to total orders, so minimal and maximal elements coincide with minimum and maximum, 
        respectively.
    """
    discard = set()

    for m in A:
        for x in A:
            if (m, x) not in P:
                discard.add(m)
                break
    
    minimal = set(A - discard)
    discard.clear()

    for n in A:
        for x in A:
            if (x, n) not in P:
                discard.add(n)
                break

    maximal = set(A - discard)
    
    return minimal, maximal

def cotas(P: set, A: set, B: set):
    """
    The function `cotas` calculates the lower and upper bounds of a set based on two other sets and a
    given relation.
    """

    discard = set()
    lower_bound = set()
    upper_bound = set()

    for a in A:
        for b in B:
            if (a, b) not in P:
                discard.add(a)
                break
    
    lower_bound = set(A - discard)
    discard.clear()

    for a in A:
        for b in B:
            if (b, a) not in P:
                discard.add(a)
                break
    
    upper_bound = set(A - discard)

    return lower_bound, upper_bound

def extremos(P: set,lower_bound: set, upper_bound: set):
    """
    The function `extremos` takes three sets as input (P, lower_bound, upper_bound) and returns two sets
    containing elements that are the lower and upper bounds of P.
    """
    discard = set()

    for m in upper_bound:
        for x in upper_bound:
            if (m, x) not in P:
                discard.add(m)
                break
    
    sup = set(upper_bound - discard)
    discard.clear()

    for n in lower_bound:
        for x in lower_bound:
            if (x, n) not in P:
                discard.add(n)
                break

    inf = set(lower_bound - discard)

    return inf, sup