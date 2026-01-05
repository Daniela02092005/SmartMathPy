from utils import convertir_valores

funcion = input("Ingrese la función a evaluar en términos de a con espacios entre cada término: ").split()

cantidad = int(input("Ingrese la cantidad de imágenes que desea encontrar: "))

    
def evaluar_funcion(f, d):
    print(f, d)

    resultados = {}

    for elemento in d:
        nueva_funcion = []
        for token in f: # La función la tengo con split y eso devuelve tokens, por eso evaluo cada token
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

dominios = []
for c in range(cantidad):
    valor = input(f"Ingrese el {c+1} dominio a encontrar: ")
    dominio = convertir_valores(valor)
    dominios.append(dominio)

respuesta = evaluar_funcion(funcion, dominios)

print("Solución final: ", respuesta)