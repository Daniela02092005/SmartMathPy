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

def diferencia_simetrica(A: set, B: set):
    """
    The function `diferencia_simetrica` calculates the symmetric difference between two sets A and B by
    finding elements that are only in one of the sets.
    """

    try:
        primera_parte = diferencia_conjuntista(A, B)
    except:
        primera_parte = set() #Dado el caso de que se ejecute el error en la función diferencia_conjuntista

    try:
        segunda_parte = diferencia_conjuntista(B, A)
    except:
        segunda_parte = set() #Dado el caso que se ejecute el error en la funcion diferencia_conjuntista

    resultado = union(primera_parte, segunda_parte)

    return resultado

def contenido(A: set, B: set):
    """
    The function checks if all elements in set A are also present in set B and returns True if they are,
    otherwise False.
    """
    resultado = True

    for elemento in A:
        if elemento in B:
            resultado = True
        else:
            resultado = False
            break

    return resultado

def contenido_estrictamente(A: set, B: set):
    """
    The function `contenido_estrictamente` checks if set A is strictly contained in set B.
    """
    resultado = contenido(A, B)
    if resultado == True and A != B:
        resultado = True
    else:
        resultado = False

    return resultado

def complemento(R: set, A: set):
    """
    The function `complemento` takes two sets `R` and `A`, and returns the set difference between `R`
    and `A`.
    """
    resultado = diferencia_conjuntista(R, A)
    return resultado

def conjunto_de_partes(A: set):
    """
    The function creates the power set of a given set A.
    """
    vacio = tuple()

    conjunto_partes = set()
    conjunto_partes.add(vacio)

    for elemento in A:
        copia = conjunto_partes.copy()
        for subconjunto in copia:
            copia_subconjunto = list(subconjunto)
            copia_subconjunto.append(elemento)
            nuevo_subconjunto = tuple(copia_subconjunto)
            conjunto_partes.add(nuevo_subconjunto)

    return conjunto_partes

def producto_cartesiano(A: set, B: set):
    """
    The function `producto_cartesiano` takes two sets as input and returns the Cartesian product of the
    two sets as a set of tuples.
    """
    resultado = set()

    for elementoA in A:
        for elementoB in B:
            a = elementoA
            b = elementoB
            par_ordenado = (a,b)
            resultado.add(par_ordenado)

    return resultado