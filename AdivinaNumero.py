import random # aleatorio

def adivina_el_numero(x):
    
    print("Bienvenido al Juego")
    print("Tu meta es adivinar el numero generado por la computadora.")

    numero_aleatorio= random.randint(1,x) # Numero aleatorio entre 1 y x
    # random.randint(a,b) Retorna un entero aleatorio N tal que a <= N <= b 

    prediccion= 0 

    while prediccion != numero_aleatorio:
        prediccion= int(input(f"Adivina un numero entre 1 y {x}: "))

        if prediccion <numero_aleatorio:
            print("Intenta otra vez. EL numero es muy pequeño.")
        elif prediccion > numero_aleatorio :
            print("Inenta otra vez. Este numero es muy grande.")
    
    print(f"¡Felicidades ! Adivinaste el numero {numero_aleatorio} correctamente")


adivina_el_numero(10)

