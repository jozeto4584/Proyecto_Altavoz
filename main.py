import random
import re 

bandas = []
opcion = 100

print("*****FESTIVAL ALTAVOZ*****")
print("**************************")

while opcion != 6:
        
    print("1. Registrar Banda ")
    print("2. Cartel Festival")
    print("3. Buscar Banda")
    print("4. Modificar Una Banda")
    print("5. Eliminar Banda")
    print("6. Finalizar")

    try:
        opcion = int(input("Digita una opcion: "))
    except ValueError:
        print("Por favor, ingresa un número entero.")
        continue
    
    if opcion == 1:
        banda = {}
                
        banda["id"] = random.randint(1, 100)  
        banda["nombre"] = input("Nombre Banda: ")
        banda["genero"] = input("Género: ")
        banda["costo"] = int(input("Costo: "))
               
        bandas.append(banda)
         
    elif opcion == 2:
        
        if bandas:
            print("****BIENVENIDO A NUESTRO FESTIVAL DE ALTAVOZ****")
            print("*** Estas son nuestras bandas que estarán en nuestro evento ***")
                        
            for bandaAuxiliar in bandas:
                print(f"{bandaAuxiliar['id']} -- {bandaAuxiliar['nombre']}")
        else:
            print("No hay bandas registradas en el festival.")
        
    elif opcion == 3:
       
        bandaBuscada = input("Digita el nombre de la banda que quieres buscar: ")
        encontrado = False
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"].lower() == bandaBuscada.lower():
                print("¡La encontré!")
                print(f"Nombre: {bandaAuxiliar['nombre']}, Género: {bandaAuxiliar['genero']}, Costo: {bandaAuxiliar['costo']}")
                encontrado = True
                break  
            print("No se encontró la banda.")
            
    elif opcion == 4:
        id_modificar = int(input("Ingrese ID de la banda a modificar: "))
        found = False
        for banda in bandas:
            if banda["id"] == id_modificar:
                found = True
                
                print(f"modificar banda ID :{banda['id']}")
                banda["nombre"]=input("Nuevo nombre de la banda : ")
                banda["genero"]= input("Nuevo genero :")
                
                while True:
                    clasificacion =input("Nueva clasificacion (1. Amateur, 2. Inermedio, 3. Especiales ) :")
                    if clasificacion in['1','2','3']:
                        banda["clsificacion"]= int (clasificacion)
                        break
                    else:
                        print("clasifiacacion no valida. Debe ser entre 1 y 3.")
                        
                        
                while True:
                    
                    tiempo =input("Nuevo tiempo en el escenario (fomato HH:MM : ) ") 
                    if re.match(r'^\d{1,2}:\d{2}$', tiempo):
                        banda["tiempo"]= tiempo
                        break  
                    
                    else: 
                        print("Formato de tiempo invalido Debe ser HH:MM.")
               
                while True:
                    try:
                       banda["costo"] = int(input("Nuevo Costo : $"))
                       break    
                    except ValueError:
                        
                        
                       print("Por favor, ingrese un valor numero para el costo :")  
                
                
               
               
                print("banda modicicada con exito")
             
        if  not found:
            print("banda no encontrada ")    
        
    elif opcion == 5:
        id_eliminar = int (input("Ingrese el ID de la banda que deseea eliminar: "))
        found = False
        for i, banda in enumerate(bandas):
            if banda["id"] == id_eliminar:
                found = True
                del bandas[i]
                print("banda Eliminda exotosamente.")
                       
            if not found:
                print("Banda no enconteadada.")
    
    elif opcion == 6:
        print("¡Vuelva Pronto!") 
           
    else: print("Opcion  Invalida. Por Favor Digite Un numero entre  1 Y 6 .")    
                      
