dicc = {}
def agregar_info():
    cantidad = int(input("¿Cuánta información deseas agregar? "))
    for i in range(cantidad):
        clave = input(f"Ingrese la clave #{i + 1}: ")
        valor = input(f"Ingrese el valor para la clave '{clave}': ")
        dicc[clave] = valor
    print("Información agregada exitosamente.")

def modificar_info(clave, nuevo_valor):
    if clave in dicc:
        dicc[clave] = nuevo_valor
        print("Información modificada exitosamente.")
    else:
        print("La clave no existe en el diccionario.")

def imprimir_info():
    if dicc:
        print("Información almacenada:")
        for clave, valor in dicc.items():
            print(clave + ":", valor)
    else:
        print("No hay información almacenada.")

while True:
    print("\n--- Menú ---")
    print("1. Agregar información")
    print("2. Modificar información")
    print("3. Imprimir información")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_info()
    elif opcion == "2":
        clave = input("Ingresa la clave de la información que deseas modificar: ")
        nuevo_valor = input("Ingresa el nuevo valor de la información: ")
        modificar_info(clave, nuevo_valor)
    elif opcion == "3":
        imprimir_info()
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")
