#Modificar Listas
lista3=["a","b","c","d","e","f","g"]
lista3.append("h") #inserta al final
print(lista3)
print(len(lista3)) #Logitud de la lista
lista3.insert(1,"z")
print(lista3)

# Metodos de Lista
lista= [8,90,1,5,8,56,4,2,6]
lista.sort() # organiza la lista
print(lista)
lista.sort(reverse=True)
print(lista)
#Numero menor
print(min(lista))
#Numero Mayor
print(max(lista))

#Comprobando si un numero esta en la lista
print(5 in lista)
#Comprobando que el numero no este  en la lista
print(5 not in lista)
# Index 
index = lista3.index("h")
print(index)
# Matrices
columna_a=[10,20]
columna_b=[30,40]
matrices=[columna_a,columna_b]
print(matrices)
print(matrices[0][0]) # Primer elemento de la matrices