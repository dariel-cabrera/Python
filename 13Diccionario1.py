# Get
elementos={'a':1,'b':2,'c':3,'d':4}
valor= elementos.get('d')
print(valor)
valor=elementos.get('z')
print(valor)

#setdefault
valor=elementos.setdefault('e',5) # va a retornar el valor de la llave si no existe lo aagrega

# Eliminar Elementos
diccionario3= {'a': 1, 'b':2,'c':3,'d':4}
del diccionario3 ['a'] #elimina el elemento
print(diccionario3)
valor4= diccionario3.pop('b') #retorna el elemento
print(valor4)
diccionario3.clear() # elemina todos los elementos
print(diccionario3)