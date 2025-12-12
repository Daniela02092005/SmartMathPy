def convertir_valores(valor: str):
    """
    The function `convertir_valores` in Python converts a string value into either an integer, float, or
    fraction.
    """

    # Fracciones
    if "/" in valor:
        partes = valor.split("/")
        if len(partes) != 2:
            raise ValueError("La fracción debe estar compuesta por 2 partes, numerador y denominador.")
        
        numerador, denominador = partes
        if "." in numerador:
            numerador = float(numerador)
        else:
            numerador = int(numerador)

        if "." in denominador:
            denominador =float(denominador)
        else:
            denominador = int(denominador)

        if denominador == 0:
            raise ZeroDivisionError("El denominador debe ser diferente de cero")
        
        return numerador, denominador
        
    # Decimales
    elif "." in valor:
        try:
            return float(valor)
        except ValueError:
            raise ValueError(f"Valor inválido {valor}")
        
    # Entero
    else:
        try:
            return int(valor)
        except ValueError:
            raise ValueError(f"Valor inválido {valor}")
        
def convertir_a_fraccion(valor: str):
    parte_entera, parte_decimal = valor.split(".")

    cantidad_decimales = len(parte_decimal)

    denominador = 10**cantidad_decimales

    numerador_string = parte_entera + parte_decimal
    numerador = int(numerador_string)

    return numerador, denominador