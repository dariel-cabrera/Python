# String con Listados
lenguajes= "Python Ruby Java Rust C++ C "
lista_lenguajes= lenguajes.split()
print(lista_lenguajes)
lista_lenguajes1= lenguajes.split('-')
print(lista_lenguajes1)
lista_lenguajes2= lenguajes.split('-',2)
print(lista_lenguajes2)

lenguajes=["Python"," Ruby" ,"Java"," Rust"," C++","C "]
string_lenguajes=' '.join(lenguajes)
print(string_lenguajes)

# Validar sub string
titulo_curso= 'Curso Profesional de Python'
contador= titulo_curso.count('Python') # Cuanta las veces que aprece la palabra o caracteres
print("La cantidad de veces que aparece la palabra es",contador)
print('Python' in titulo_curso) # in devuelve un valor boleano
print('python' in titulo_curso.lower()) #lower convierte todo a minuscula
print('codigo facilito' not in titulo_curso.lower()) # Podemos negar
#endswitch
#startswitch