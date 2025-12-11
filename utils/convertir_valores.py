def convertir_valores(valor):
    if "/" in valor:
        numerador, denominador = valor.split("/")
        return int(numerador) / int(denominador)
    elif "." in valor:
        return float(valor)
    else:
        return int(valor)