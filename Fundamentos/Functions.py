from utils import convert_values
    
def evaluate_function(function: list, domains: list):
    """
    The function evaluates a mathematical expression with variables replaced by values from a given
    domain.
    """
    

    results = {}

    for element in domains:
        new_function = []
        for token in function: 
            if token == "a":
                new_function.append(element)
            elif token in ["+", "-", "*", "**", "(", ")", "/"]:
                new_function.append(token)
            else:
                converted_function = convert_values(token)
                new_function.append(converted_function)
        print(f"Función reemplazando a por {element}: ",new_function)

        while "**" in new_function:
            i = new_function.index("**")
            result = new_function[i-1] ** new_function[i+1]
            new_function[i-1:i+2] = [result]
            print("Potencia resuelta: ",result)

        while "*" in new_function or "/" in new_function:
            if "*" in new_function:
                i = new_function.index("*")
                result = new_function[i-1] * new_function[i+1]
                new_function[i-1:i+2] = [result]
                print("Multiplicación resuelta: ",result)
            else:
                i = new_function.index("/")
                result = new_function[i-1] / new_function[i+1]
                new_function[i-1:i+2] = [result]
                print("División resuelta: ",result)

        while "+" in new_function or "-" in new_function:
            if "+" in new_function:
                i = new_function.index("+")
                result = new_function[i-1] + new_function[i+1]
                new_function[i-1:i+2] = [result]
                print("Suma resuelta: ",result)
            else:
                i = new_function.index("-")
                result = new_function[i-1] - new_function[i+1]
                new_function[i-1:i+2] = [result]
                print("Resta resuelta: ", result)
    
        results[element] = new_function[0]

    return results

def classification(A: set, B: set, function):
    """
    The function takes two sets A and B, along with a function, and determines if the function is
    injective, surjective, or bijective.
    """

    image = []
    injective = True
    surjective = True
    bijective = True

    for value in A:
        a = value
        classification = eval(function)
        image.append(classification) 

    print("Image =", image)

    # This part of the code is checking whether the function is injective or not. Here's a breakdown
    # of what it's doing:

    set_image = set(image) 

    if len(image) == len(set_image): #Si el set no eliminó nada es porque no habían repeticiones, condición de la inyectiva
        injective = True
    else:
         injective = False

    # This part of the code is checking whether the function is surjective (also known as onto) or
    # not. Here's a breakdown of what it's doing:

    auxiliary = []
    auxiliary = set(B).difference(set(image)) 
    if len(auxiliary) != 0: 
        surjective = False
    else:
        surjective = True

    # The code snippet `if injective == True and surjective == True:` is checking if both the
    # conditions for a function to be bijective are met.
    
    if injective == True and surjective == True:
        bijective = True
    else:
        bijective = False
        
    return f"Injective {injective}, surjective {surjective} y bijective {bijective}"