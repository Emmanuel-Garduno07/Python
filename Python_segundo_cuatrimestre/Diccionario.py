estudiante = {
    "Nombre": "Juan Perez",
    "Carrera": "Software",
    "Edad": "21",
    "Localidad": "Lazaro Cardenas",
    "Promedio": "8.5"
}

def mostrar_datos():
    print("\nDatos actuales del estudiante:")
    for clave, valor in estudiante.items():
        print(clave + ":", valor)

mostrar_datos()

while True:
    modificar = input("\n¿Deseas modificar algún dato? (s/n): ").lower()
    
    if modificar == "s":
        campo = input("¿Qué dato quieres modificar? (Nombre, Carrera, Edad, Localidad, Promedio): ").capitalize()
        if campo in estudiante:
            nuevo_valor = input("Ingresa el nuevo valor para " + campo + ": ")
            estudiante[campo] = nuevo_valor
            print(campo, "ha sido actualizado.")
            mostrar_datos()  
        else:
            print("El campo ingresado no es valido.")
    elif modificar == "n":
        print("Gracias Aquí tienes la información final.")
        mostrar_datos() 
        break
    else:
        print("Por favor, responde con 's' o 'n'.")

print("\nInformación final del estudiante:")
mostrar_datos()

