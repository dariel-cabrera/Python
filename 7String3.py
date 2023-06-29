#Justificar Texto
mensaje='Hola mundo'
# ljust -> Justificar a la Izquierda.
# rjust ->Justificar a la Derecha
# Center-> Centrar 

mensaje1= mensaje.rjust(20) # <- 20 Cantidad de espacios a la izquierda
print('!',mensaje1)
mensaje2= mensaje.ljust(20) # <- 20 Cantidad de espacios a la derecha
print(mensaje2,'!')
mensaje3= mensaje.center(20) #<- 10 a la izquierda MENSAJE  10 a la derecha
print('!',mensaje3,'!') 

# Metodos de String 
animal= "Blanquito Feliz"
animal2="   Lulita Feliz    "
animal3=" Canela Feliz "
print(animal.upper( ) ) #Convierte todo a Mayuscula
print(animal.lower() )  #Convierte todo a minuscula 
print(animal.title( ) ) #Convierte  los primeros caracteres de cada palabra a Mayusc
#Quita los espacios que estan a la derecha y la izquierda 
print(animal2.strip( ) )
print(animal3.strip( ).capitalize( ) )
# Quita los espacios de la izquierda 
print(animal2.lstrip( ) )
#Quita los espacios de la derecha
print(animal3.rstrip( ) )
# find Para buscar una cadena de caracteres dentro de otra cadena de caracteres devuelve un indice positivo si lo q devuelve es un numero negativo es q no lo encontro
n1= animal.find("q") 
if n1 > 0:
   print("Encontrado")
else:
    print("No esta")

# Cambiar una cadena de caracteres por otra 
print(animal.replace("B","v" ) )
