# Tuplas
# NO pueden Modificarse
# Pueden almacenar dif tipos de Datos  y Otras Tuplas
tuplas=("String",10,15.4,True,[1,2,3])
print(tuplas)
# Indices 
curso=("C++","Python","Java","Javapscri","Node")
primer_curso=curso[0] #primer elemento
segundo_curso=curso[-1]#utlimo elemntos
print(primer_curso)
print(segundo_curso)

#Lista y Tuplas
curso=["C++","Python","Java"]
niveles=("Basico","Intermedio","Avanzado")
curso_tuplas= tuple(curso)
print(curso_tuplas)
niveles_lista=list(niveles)
print(niveles_lista)