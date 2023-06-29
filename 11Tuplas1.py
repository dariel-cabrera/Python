# Desempaquetando
numeros=(1,2,3,4,5)
uno,dos,tres,cuatro,cinco= numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
numeros=(1,2,3,4,5,6,7,8,9)
uno,dos,tres,cuatro,cinco,*resto_valores= numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(resto_valores)
# uno,dos,tres,cuatro,cinco,_= numeros
#print(uno)
#print(dos)
#print(tres)
#print(cuatro)
#print(cinco)
#print(_)
#Zip (Comprimir)
lista=[1,2,3,4,5]
tupla=(10,20,30,40,50)
resultado=zip(tupla,lista)
resultado=tuple(resultado)
print(resultado)
resultado=zip(lista,tupla)
print(resultado)
lista_2=[100,200,300,400,500]
#resultado=zip(lista,tupla,lista_2)
#print(resultado)