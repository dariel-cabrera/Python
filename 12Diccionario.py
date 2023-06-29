# Diccionario
diccionario={"total":55,"descuento": True,"subtotal":15}
diccionario2={"total":55,10:"Curso de Python",(1,2,3):True}

# Se puede usar clases como Llaves
usuario={
    "nombre":"Nombre del usuario",
    "edad":23,
    "curso":"Curso de Python",
    "skills":{
        "programacion":True,
        "base_de_datos":False
        },
    "medallas":["basico","intermedio"]
    }

print(usuario)
# Agregar Nuevo valor a una Llave
usuario["nombre"]="Eduardo"
print(usuario)
# Obtener valor mediante una llave
print(usuario["curso"])
diccionario={"Eduardo":1,"Fernando":2,"Uriel":3,"Rafael":4}
d1=diccionario.keys()
print(d1)
d2= diccionario.values()
print(d2)
for key,value in diccionario.items():
    print(key,value)

# Logitud de un Diccionario
elementos={}
elementos['nombre']="Cody" #Las llaves son inmutables. No pueden Modificarse
print("La longitud de el diccionario es",len(elementos))
# Modificando los valores de una llave
elementos['nombre']='CodigoFacilito'
print(elementos['nombre']) # En caso que la llave no exista.Python la crea

#¿Que sucede si una llave esta duplicada
elementos={'a':1,'b':2,'c':3,'a':4} #La llave repetida toma el valor ultimo asignado
print(elementos) 

# Obtener elementos 
elementos={'a':1,'b':2,'c':3,'d':4}
valor=elementos['d']
print(valor)

#Para evitar que no entre una llave que no se encuentre en el diccionario
print('z' in elementos)

