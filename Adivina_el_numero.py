import random

def adivina_el_numero_computadora(x):
    print(" ¡Bienvenido al Juego! ")
    print(f"Selecciona un numero entre 1 y {x} para que la cumputadora intente adivinarlo")

    limite_inferior= 1
    limite_superior= x

    respuesta= ""

    while respuesta != "c":
        #generar prediccion
        if limite_inferior != limite_superior: 
            prediccion = random.randint(limite_inferior,limite_superior)
        else:
            prediccion= limite_inferior

        #Obtener respuesta del usuario
        respuesta= input(f"Mi prediccion es {prediccion}.Si es muy alta,ingresa (A). Si es muy baja, ingresa (B).Si es correcta, ingresa (C)").lower()
    
        if respuesta == "a":
            limite_superior= prediccion-1
        elif respuesta== "b":
            limite_inferior= prediccion+1

    print(f"Siii! La computadora lo adivino")

adivina_el_numero_computadora(100)
    

