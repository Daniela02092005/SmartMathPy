from Conjuntos import producto_cartesiano, contenido, interseccion

def diagonal(A: set):
    """
    The function `diagonal` takes a set as input and returns a set of tuples where each tuple contains
    an element from the input set repeated twice.
    """
    resultado = set()

    for a in A:
        par_ordenado = (a, a)
        resultado.add(par_ordenado)

    return resultado

def compuesta(A: set, B: set, C: set):
    """
    The function `compuesta` takes three sets A, B, and C, computes the Cartesian products of A and B,
    and B and C, then finds pairs of elements where the second element of the first pair matches the
    first element of the second pair, returning a set of resulting pairs.
    """
    S = producto_cartesiano(A, B)
    T = producto_cartesiano(B, C)
    resultado = set()

    for s in S:
        DomS = s[0]
        RanS = s[1]
        for t in T:
            DomT = t[0]
            RanT = t[1]
            if RanS == DomT:
                par_ordenado = (DomS, RanT)
                resultado.add(par_ordenado)
    
    return resultado

def inversa(A: set, B: set):
    """
    The function inversa takes two sets A and B, computes the Cartesian product of A and B, and returns
    a new set with the pairs reversed.
    """
    original = producto_cartesiano(A, B)
    resultado = set()

    for par in original:
        nuevo_par = (par[1], par[0])
        resultado.add(nuevo_par)
    
    return resultado

def reflexiva(Diagonal: set, R: set):
    """
    The function checks if a relation R is reflexive based on the elements in the diagonal set.
    """
    if contenido(Diagonal, R) == True:
        return True
    else:
        return False
    
def simetrica(Inversa: set, R: set):
    """
    The function `simetrica` checks if two sets are equal and returns True if they are, otherwise
    returns False.
    """
    if Inversa == R:
        return True
    else:
        return False
    
def transitiva(Compuesta: set, R: set):
    """
    The function `transitiva` checks if a set `Compuesta` contains all elements of another set `R`.
    """
    if contenido(Compuesta, R) == True:
        return True
    else:
        return False
    
def antisimetrica(R: set, Inversa: set, Diagonal: set):
    """
    The function checks if the intersection of two sets is contained within a third set.
    """
    a = interseccion(R, Inversa)
    
    if contenido(a, Diagonal):
        return True
    else:
        return False