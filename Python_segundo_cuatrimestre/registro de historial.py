pila = []

def agregar_busqueda():
    """Agrega una búsqueda al tope de la pila."""
    busqueda = input("¿Qué quieres buscar? ")
    fecha = input("Ingresa la fecha (formato DD-MM-YYYY): ")
    hora = input("Ingresa la hora (formato HH:MM:SS): ")
    
    registro = {
        "busqueda": busqueda,
        "fecha": fecha,
        "hora": hora
    }
    pila.append(registro)  
    print("Se agregó: " + busqueda + " en " + fecha + " a las " + hora + ".\n")

def mostrar_pila():
    """Muestra las búsquedas en orden LIFO (última en entrar, primera en mostrarse)."""
    if not pila:
        print("La pila está vacía.\n")
    else:
        print("\nPila de búsquedas (LIFO):")
        for i, registro in enumerate(reversed(pila), 1):
            print("{}. {} - {} {}".format(i, registro['busqueda'], registro['fecha'], registro['hora']))
        print()

def eliminar_ultima_busqueda():
    """Elimina la búsqueda más reciente (tope de la pila)."""
    if pila:
        eliminado = pila.pop()  
        print("Se eliminó: " + eliminado['busqueda'] + ".\n")
    else:
        print("La pila ya está vacía.\n")

def limpiar_pila():
    """Limpia completamente la pila."""
    pila.clear()
    print("Se ha eliminado toda la pila.\n")

def navegador_simulado():
    """Menú principal del navegador simulado."""
    while True:
        print("1. Agregar búsqueda")
        print("2. Ver pila de búsquedas")
        print("3. Eliminar última búsqueda (LIFO)")
        print("4. Limpiar toda la pila")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_busqueda()
        elif opcion == "2":
            mostrar_pila()
        elif opcion == "3":
            eliminar_ultima_busqueda()
        elif opcion == "4":
            limpiar_pila()
        elif opcion == "5":
            print("Saliendo del navegador... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")
navegador_simulado()
