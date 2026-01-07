from Conjuntos import producto_cartesiano, contenido, interseccion

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
    
def comparable(P: set, a, b):
    """
    The function `comparable` determines whether two elements are comparable based on a given set of
    pairs.
    """
        
    if (a, b) in P or (b, a) in P:
        return "Comparables"
    else:
        return "Incomparables"
    
def orden_total(P: set, A: set):
    """
    The function `orden_total` checks if a given set of pairs satisfies the total order property.
    """

    resultado = True

    for a in A:
        for b in A:
            if (a, b) in P or (b, a) in P:
                continue
            else:
                resultado = False
                break

    return resultado

def minmax(P: set, A: set):
    """
    The function minmax takes two sets P and A as input, and returns the minimal and maximal elements of
    set A based on the relation defined in set P.
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
    
    lower_bound = set(A - discard) #Cota inferior = lower bound
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