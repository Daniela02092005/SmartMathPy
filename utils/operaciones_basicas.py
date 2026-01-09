from Convert_values import convert_values, convert_to_fraction

'''
    Este módulo contiene implementaciones elementales de operaciones aritméticas utilizando técnicas imperativas básicas. 
    Su propósito es didáctico; el resto del proyecto utiliza los operadores aritméticos nativos de Python.
'''

def multiplicacion(a, b):
    resultado = 0
    for i in range(b):
        resultado = resultado + a
    return resultado

def suma(a, b):
    sumando1 = convert_values(a)
    sumando2 = convert_values(b)

    if isinstance(sumando1, int) and isinstance(sumando2, int): #isinstance verifica que el objeto sea del timpo que se está preguntando
        auxiliar = []
        for i in range(sumando1):
            auxiliar.append(i)
        for i in range(sumando2):
            auxiliar.append(i)
        return len(auxiliar)
    
    else:
        if isinstance(sumando1, float) and isinstance(sumando2, float):
            fraccion1 = convert_to_fraction(str(sumando1))
            fraccion2 = convert_to_fraction(str(sumando2))

            numerador1, denominador1 = fraccion1
            numerador2, denominador2 = fraccion2

            if denominador1 == denominador2:

                a = suma(numerador1, numerador2)
                b = denominador2

                return a / b

            else:
                a = multiplicacion(numerador1, denominador2)
                b = multiplicacion(numerador2, denominador1)
                c = multiplicacion(denominador1, denominador2)

                ab = suma(a, b)

                return ab / c

def resta(a, b):
    minuendo = convert_values(a)
    sustraendo = convert_values(b)

    if isinstance(minuendo, int) and isinstance(sustraendo, int): 
        auxiliar = []
        for i in range(minuendo):
            auxiliar.append(i)
        for i in range(sustraendo):
            auxiliar.pop()
        return len(auxiliar)
    
    else:
        if isinstance(minuendo, float) and isinstance(sustraendo, float):
            fraccion1 = convert_to_fraction(str(minuendo))
            fraccion2 = convert_to_fraction(str(sustraendo))

            numerador1, denominador1 = fraccion1
            numerador2, denominador2 = fraccion2

            if denominador1 == denominador2:

                a = resta(numerador1, numerador2)
                b = denominador2

                return a / b

            else:
                a = multiplicacion(numerador1, denominador2)
                b = multiplicacion(numerador2, denominador1)
                c = multiplicacion(denominador1, denominador2)

                ab = resta(a, b)

                return ab / c    

def exponente(a, b):
    resultado = 1
    for i in range(b):
        resultado = multiplicacion(resultado, a)
    return resultado