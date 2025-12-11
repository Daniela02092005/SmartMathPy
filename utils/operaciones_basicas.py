class operaciones_basicas():
    def suma(self, *elementos): # *elementos = argumento arbitrario en tupla, porque no sé cuantos argumentos le pasarán a la función
        lista = list(elementos) # Convierto la tupla en lista

        tamano = len(lista) # Reviso el tamaño de la lista
        suma = []

        for t in range(tamano):
            indice = lista[t]
            for i in indice:
                suma.append(i)
        return len(suma)
    
    def resta(self, *elementos): # *elementos = argumento arbitrario en tupla, porque no sé cuantos argumentos le pasarán a la función
        lista = list(elementos) # Convierto la tupla en lista

        primer_valor = float(lista[0]) # Guardo el primer valor de la lista
        resta = [] 

        for p in primer_valor:
            resta.append(p) #Relleno la lista con ese valor
        
        tamano = len(lista)
        auxiliar = []

        for t in range(1, tamano):
            auxiliar.append(lista[t])
        resultado = self.suma(auxiliar)

        for r in resultado:
            resta.pop()