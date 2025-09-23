# This block of code is prompting the user to input the sizes of two sets, A and B, and then proceed
# to input the elements of each set.

tamanoA = int(input("Ingrese el tamaño del conjunto A: "))
tamanoB = int(input("Ingrese el tamaño del conjunto B: "))

print("Empecemos por el conjunto A")
conjuntoA = []
for i in range(tamanoA):
    conjuntoA.append(int(input("Ingrese el elemento: ")))

print("Continuemos con el conjunto B")
conjuntoB = []
for i in range(tamanoB):
    conjuntoB.append(int(input("Ingrese el elemento: ")))

funcion = input("Ingrese la función f(a) en términos de a: ")

def clasificacion(A,B,f):
    """
    This Python function evaluates a given function for each element in a set A and stores the results
    in a list called "imagen".
    
    :param A: A is a set of elements from which the function will take input values
    :param B: It seems like the parameter `B` is missing in the function `clasificacion`. Could you
    please provide the definition or values of the set `B` so that I can assist you further with the
    function?
    :param f: The parameter `f` in the `clasificacion` function is a string representing a mathematical
    function. It could be something like "2*a + 3" or "a**2 - 1". This function will be evaluated for
    each element in the set `A` to determine the image of
    """

    imagen = []
    inyectiva = True
    sobreyectiva = True

    for valor in A:
        a = valor #toma el valor del conjunto que corresponde a la iteración
        resultado_funcion = eval(f) # Evalua la función que digitó el usuario
        imagen.append(resultado_funcion) 

    print("Imagen =", imagen)

    # This part of the code is checking whether the function is injective or not. Here's a breakdown
    # of what it's doing:

    set_imagen = set(imagen) 

    if len(imagen) == len(set_imagen): #Si el set no eliminó nada es porque no habían repeticiones, condición de la inyectiva
        inyectiva = True
        print("Es inyectiva")
    else:
         inyectiva = False
         print("No es inyectiva")

    # This part of the code is checking whether the function is surjective (also known as onto) or
    # not. Here's a breakdown of what it's doing:

    auxiliar = []
    auxiliar = set(B).difference(set(imagen)) 
    if len(auxiliar) != 0: 
        sobreyectiva = False
        print("No es sobreyectiva")
    else:
        sobreyectiva = True
        print("Es sobreyectiva")

    # The code snippet `if inyectiva == True and sobreyectiva == True:` is checking if both the
    # conditions for a function to be bijective are met.
    
    if inyectiva == True and sobreyectiva == True:
        print("Es biyectiva")
    else:
        print("No es biyectiva")
        
clasificacion(conjuntoA,conjuntoB, funcion)
