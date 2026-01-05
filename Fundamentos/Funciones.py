from utils import convertir_valores
    
def evaluar_funcion(function: list, domains: list):
    """
    The function evaluates a mathematical expression with variables replaced by values from a given
    domain.
    """

    resultados = {}

    for elemento in domains:
        nueva_funcion = []
        for token in function: # La función la tengo con split y eso devuelve tokens, por eso evaluo cada token
            if token == "a":
                nueva_funcion.append(elemento)
            elif token in ["+", "-", "*", "**", "(", ")", "/"]:
                nueva_funcion.append(token)
            else:
                funcion_convertida = convertir_valores(token)
                nueva_funcion.append(funcion_convertida)
        print(f"Función reemplazando a por {elemento}: ",nueva_funcion)

        while "**" in nueva_funcion:
            i = nueva_funcion.index("**")
            resultado = nueva_funcion[i-1] ** nueva_funcion[i+1]
            nueva_funcion[i-1:i+2] = [resultado]
            print("Potencia resuelta: ",resultado)

        while "*" in nueva_funcion or "/" in nueva_funcion:
            if "*" in nueva_funcion:
                i = nueva_funcion.index("*")
                resultado = nueva_funcion[i-1] * nueva_funcion[i+1]
                nueva_funcion[i-1:i+2] = [resultado]
                print("Multiplicación resuelta: ",resultado)
            else:
                i = nueva_funcion.index("/")
                resultado = nueva_funcion[i-1] / nueva_funcion[i+1]
                nueva_funcion[i-1:i+2] = [resultado]
                print("División resuelta: ",resultado)

        while "+" in nueva_funcion or "-" in nueva_funcion:
            if "+" in nueva_funcion:
                i = nueva_funcion.index("+")
                resultado = nueva_funcion[i-1] + nueva_funcion[i+1]
                nueva_funcion[i-1:i+2] = [resultado]
                print("Suma resuelta: ",resultado)
            else:
                i = nueva_funcion.index("-")
                resultado = nueva_funcion[i-1] - nueva_funcion[i+1]
                nueva_funcion[i-1:i+2] = [resultado]
                print("Resta resuelta: ", resultado)
    
        resultados[elemento] = nueva_funcion[0]

    return resultados

def clasificacion(A: set, B: set, function):

    """
    The function clasificacion determines if a given function is injective, surjective, and bijective
    based on sets A and B and the function provided.
    """

    imagen = []
    inyectiva = True
    sobreyectiva = True
    biyectiva = True

    for valor in A:
        a = valor #toma el valor del conjunto que corresponde a la iteración
        resultado_funcion = eval(function) # Evalua la función que digitó el usuario
        imagen.append(resultado_funcion) 

    print("Imagen =", imagen)

    # This part of the code is checking whether the function is injective or not. Here's a breakdown
    # of what it's doing:

    set_imagen = set(imagen) 

    if len(imagen) == len(set_imagen): #Si el set no eliminó nada es porque no habían repeticiones, condición de la inyectiva
        inyectiva = True
    else:
         inyectiva = False

    # This part of the code is checking whether the function is surjective (also known as onto) or
    # not. Here's a breakdown of what it's doing:

    auxiliar = []
    auxiliar = set(B).difference(set(imagen)) 
    if len(auxiliar) != 0: 
        sobreyectiva = False
    else:
        sobreyectiva = True

    # The code snippet `if inyectiva == True and sobreyectiva == True:` is checking if both the
    # conditions for a function to be bijective are met.
    
    if inyectiva == True and sobreyectiva == True:
        biyectiva = True
    else:
        biyectiva = False
        
    return f"Inyectiva {inyectiva}, sobreyectiva {sobreyectiva} y biyectiva {biyectiva}"