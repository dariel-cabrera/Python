# lista=[] ó lista=list()
lista=["String", 10, 10.5, True]
print(lista)

lista1=["Eduardo", "Pablo", "Julio","Abril"]
print(lista1)
primer_nombre= lista1[0]
print(primer_nombre)
#Actualizar elementos
lista1[3]='Marcos'
print(lista1)
#Sublistas
lista2=["a","b","c","d"]
sub_lista= lista2[0:3]
print(sub_lista)
sub_lista2=lista2[1:100]
print(sub_lista2)
sub_lista3=lista2[1:]
print(sub_lista3)
lista3=["a","b","c","d","e","f","g"]
sublista4=lista3[1:5:2] # 2 indica el salto  
print(sublista4)
sublista4=lista3[:]  # todos los elementos de la lista
print(sublista4)
sublista4= lista3[::-1] # invierte la lista
print(sublista4)