# Tipos de Datos
valor ="Eduardo"
tipo= type(valor)
print(tipo) 

# Leer valores por teclado
nombre_completo= input("Ingrese su nombre completo")
print("Su Nombre es: " ,nombre_completo)

# Convertir Tipos de Datos
edad = int(input("Ingresa tu edad"))
altura=float(input("Ingresa tu altura"))
autorizacion=input("¿autoriza el programa ?  (si/no)" ) == 'si'

print("La edad es: ", edad)
print("La altura es: ", altura)
print("Autorizo", autorizacion)
# Crear Multiples Variables 
nombre, apellidos, titulo = "Eduardo","garcia","Mr."