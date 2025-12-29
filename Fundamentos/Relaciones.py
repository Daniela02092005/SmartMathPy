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

def inversa_relacion(R: set):
    resultado = set()

    for a, b in R:
        inversa = (b,a)
        resultado.add(inversa)

    return resultado

def reflexiva(A: set, R: set):
    """
    The function checks if a relation R is reflexive based on the elements in the diagonal set.
    """
    Diagonal = diagonal(A)

    if contenido(Diagonal, R):
        return True
    else:
        return False
    
def simetrica(R: set):
    """
    The function `simetrica` checks if two sets are equal and returns True if they are, otherwise
    returns False.
    """
    Inversa = inversa_relacion(R)

    if Inversa == R:
        return True
    else:
        return False
    
def transitiva(R: set):
    """
    The function `transitiva` checks if a set `Compuesta` contains all elements of another set `R`.
    """
    Compuesta = set()
    for (a, b) in R:
        for (c, d) in R:
            if b == c:
                par_ordenado = (a, d)
                Compuesta.add(par_ordenado)

    if contenido(Compuesta, R):
        return True
    else:
        return False
    
def antisimetrica(R: set, A: set):
    """
    The function checks if the intersection of two sets is contained within a third set.
    """
    Inversa = inversa_relacion(R)
    a = interseccion(R, Inversa)
    Diagonal = diagonal(A)

    if contenido(a, Diagonal):
        return True
    else:
        return False
    
def equivalencia(A: set, R: set):
    """
    The function checks if a relation R on set A is reflexive, symmetric, and transitive.
    """
    if reflexiva(A, R) and simetrica(R) and transitiva(R):
        return True
    else: 
        return False
    
def clase_equivalencia(R: set, A: set, x):
    """
    The function `clase_equivalencia` takes a relation R, a set A, and an element x, and returns a set
    of elements from A that are related to x in R.
    """
    resultado = set()

    for elemento in A:
        if (elemento, x) in R:
            resultado.add(elemento)
    
    return resultado

def disjuntos_por_pares(A: set, B: set):
    """
    The function `disjuntos_por_pares` checks if two sets A and B are disjoint by pairs.
    """
    i = interseccion(A, B)
    if A !=B and i == set():
        return True
    else:
        return False
    
def relacion_de_orden(R: set, A: set):
    """
    The function checks if a relation R on set A is reflexive, antisymmetric, and transitive.
    """
    if reflexiva(A, R) and antisimetrica(R, A) and transitiva(R):
        return True
    else: 
        return False