print("Bienvenido al Sistema De Datos")
nombre=input("Introduzca su Nombre:")
apellido=input("Introduzca su Apellido: ")
segundoApellido=input("Introduzca su Segundo Apellido: ")
nombre_completo=f'{nombre}{" "}{apellido}{" "}{segundoApellido}'
edad= int(input("Diga su edad: "))
estudiante=input("¿Es estudiante? (si/no)")=="si"
trabajador=input("¿Es trabajador?(si/no)")=="si"
altura=float(input("Diga su altura"))

if estudiante== True and trabajador==False:
        profesion="Estudiante"  
elif estudiante==True and trabajador==True:
        profesion="Estudiante y Trabajador"           
elif estudiante==False and trabajador==True:
        profesion="trabajador"    
else:
        profesion="Eres un Vago"
        

informa=f'{"Su nombre es: "}{nombre_completo}{" "}{"Su edad es: "}{edad}{" "}{"Su profesion es: "}{profesion}'
print(informa)
