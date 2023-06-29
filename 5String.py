nombre_curso= "Ultimate Python"

# Contando la cantidad de caracteres
print(len(nombre_curso))
#Obtener el Primer caracter
print(nombre_curso[0] )
# Obteniendo la primera letra 
print(nombre_curso[ 0 : 8 ]) # Utlimate 

# Obteniendo la primera palabra
print(nombre_curso[ 9 :  ]) # Python 
# Obteniendo la ultima palabra
print(nombre_curso[ : 8 ]) # Utlimate 

# Obteniendo el String Completo
print(nombre_curso[ :  ])  #"Ultimate Python" 

#Concatenar Cadenas de Caracteres
nombre = 'Dariel'
apellido='Cabrera'
nombreComple= nombre + "  " + apellido 
print(nombreComple)
# Otra via 
nombre_completo = f'{ nombre }{" "}{apellido }'
print(nombre_completo)

# Funcion print
nombre= "Dariel"
apellido= "Cabrera"
print(nombre,apellido, "Lopez")
print(nombre,apellido, "Lopez",sep="-")