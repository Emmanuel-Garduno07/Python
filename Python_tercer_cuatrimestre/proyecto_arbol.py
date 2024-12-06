class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

def agregar_raiz(arbol, nombre_raiz):
    arbol.append(Nodo(nombre_raiz))
    return f"Raíz '{nombre_raiz}' agregada al árbol."

def agregar_hijo(nodo, nombre_hijo):
    nodo.hijos.append(Nodo(nombre_hijo))
    return f"Hijo '{nombre_hijo}' agregado a '{nodo.nombre}'."

def mostrar_arbol(arbol):
    if not arbol:
        print("El árbol está vacío.")
    else:
        for raiz in arbol:
            mostrar_subarbol(raiz)

def mostrar_subarbol(nodo, nivel=0):
    if nodo is not None:
        print("    " * nivel + "- " + nodo.nombre)
        for hijo in nodo.hijos:
            mostrar_subarbol(hijo, nivel + 1)

def buscar_nodo(arbol, nombre):
    for raiz in arbol:
        encontrado = buscar_subnodo(raiz, nombre)
        if encontrado:
            return encontrado
    return None

def buscar_subnodo(nodo, nombre):
    if nodo.nombre == nombre:
        return nodo
    for hijo in nodo.hijos:
        encontrado = buscar_subnodo(hijo, nombre)
        if encontrado:
            return encontrado
    return None

def modificar_nodo(arbol, nombre_actual, nuevo_nombre):
    nodo_a_modificar = buscar_nodo(arbol, nombre_actual)
    if nodo_a_modificar:
        nodo_a_modificar.nombre = nuevo_nombre
        return f"Nodo '{nombre_actual}' modificado a '{nuevo_nombre}'."
    else:
        return "Nodo no encontrado."

def eliminar_nodo(arbol, nombre):
    for raiz in arbol:
        if raiz.nombre == nombre:
            arbol.remove(raiz)
            return f"Raíz '{nombre}' eliminada del árbol."
        nodo, mensaje = eliminar_subnodo(raiz, nombre)
        if mensaje != "Nodo no encontrado.":
            return mensaje
    return "Nodo no encontrado."

def eliminar_subnodo(nodo, nombre):
    for i, hijo in enumerate(nodo.hijos):
        if hijo.nombre == nombre:
            nodo.hijos.pop(i)
            return nodo, f"Nodo '{nombre}' eliminado."
        hijo, mensaje = eliminar_subnodo(hijo, nombre)
        if mensaje != "Nodo no encontrado.":
            return hijo, mensaje
    return nodo, "Nodo no encontrado."

def mostrar_hijos(arbol, nombre):
    nodo = buscar_nodo(arbol, nombre)
    if nodo is None or not nodo.hijos:
        return "El nodo no tiene hijos."
    nombres_hijos = [hijo.nombre for hijo in nodo.hijos]
    return "Hijos: " + ", ".join(nombres_hijos)

# Programa principal
arbol = []

# Crear automáticamente dos raíces iniciales
print("Creando raíces iniciales...")
print(agregar_raiz(arbol, "Familia López"))
print(agregar_raiz(arbol, "Familia García"))

while True:
    print("\nÁrbol Genealógico")
    print("1. Agregar raíz")
    print("2. Agregar hijo")
    print("3. Mostrar árbol")
    print("4. Modificar nodo")
    print("5. Eliminar nodo")
    print("6. Buscar nodo y mostrar hijos")
    print("7. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre_raiz = input("Ingresa el nombre de la nueva raíz: ")
        print(agregar_raiz(arbol, nombre_raiz))
    
    elif opcion == "2":
        if not arbol:
            print("Primero debes agregar al menos una raíz.")
        else:
            nombre_buscar = input("Ingresa el nombre del nodo al que deseas agregar un hijo: ")
            nodo = buscar_nodo(arbol, nombre_buscar)
            if nodo:
                nombre_hijo = input("Ingresa el nombre del hijo: ")
                print(agregar_hijo(nodo, nombre_hijo))
            else:
                print("Nodo no encontrado.")
    
    elif opcion == "3":
        print("\nÁrbol Genealógico:")
        mostrar_arbol(arbol)

    elif opcion == "4":
        if not arbol:
            print("Primero debes agregar al menos una raíz.")
        else:
            nombre_actual = input("Ingresa el nombre del nodo que deseas modificar: ")
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            print(modificar_nodo(arbol, nombre_actual, nuevo_nombre))

    elif opcion == "5":
        if not arbol:
            print("Primero debes agregar al menos una raíz.")
        else:
            nombre_eliminar = input("Ingresa el nombre del nodo que deseas eliminar: ")
            print(eliminar_nodo(arbol, nombre_eliminar))

    elif opcion == "6":
        if not arbol:
            print("Primero debes agregar al menos una raíz.")
        else:
            nombre_buscar = input("Ingresa el nombre del nodo que deseas buscar: ")
            print(mostrar_hijos(arbol, nombre_buscar))
    
    elif opcion == "7":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Intenta de nuevo.")
