def union(A: set, B: set):
    """
    The function `union` takes two sets as input and returns a new set containing all unique elements
    from both input sets.
    """
    resultado = []

    for elemento in A:
        resultado.append(elemento)
    
    for elemento in B:
        if elemento not in resultado:
            resultado.append(elemento)

    return set(resultado)


def interseccion(A: set, B: set):
    """
    The function `interseccion` takes two sets A and B as input and returns the intersection of elements
    between the two sets, raising a ValueError if there are no common elements.
    """

    resultado = []

    for elemento in A:
        if elemento in B:
            resultado.append(elemento)

    if not resultado:
        raise ValueError("A y B son disjuntos") #Disjuntos son los conjuntos que su intersección es el conjunto vacío

    return set(resultado)

def diferencia_conjuntista(A: set, B: set):
    """
    The function `diferencia_conjuntista` takes two sets A and B as input and returns the set of
    elements that are in set A but not in set B, raising a ValueError if the resulting set is empty.
    """
    resultado = []

    for elemento in A:
        if elemento not in B:
            resultado.append(elemento)

    if not resultado:
        raise ValueError("La diferencia conjuntista es 0")
    
    return set(resultado)