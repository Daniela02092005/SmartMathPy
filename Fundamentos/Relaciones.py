from Conjuntos import producto_cartesiano

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
