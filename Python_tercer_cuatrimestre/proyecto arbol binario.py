class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijo_izquierdo = None
        self.hijo_derecho = None

def agregar_hijo(nodo, nombre_hijo):
    if nodo.hijo_izquierdo is None:
        nodo.hijo_izquierdo = Nodo(nombre_hijo)
        return "Hijo izquierdo agregado."
    elif nodo.hijo_derecho is None:
        nodo.hijo_derecho = Nodo(nombre_hijo)
        return "Hijo derecho agregado."
    else:
        return "Este nodo ya tiene dos hijos."

def mostrar_arbol(nodo, nivel=0):
    if nodo is not None:
        print("    " * nivel + "- " + nodo.nombre)
        mostrar_arbol(nodo.hijo_izquierdo, nivel + 1)
        mostrar_arbol(nodo.hijo_derecho, nivel + 1)

raiz = None

while True:
    print("\nÁrbol Genealógico")
    print("1. Crear raíz")
    print("2. Agregar hijo")
    print("3. Mostrar árbol")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        if raiz is None:
            nombre_raiz = input("Ingresa el nombre de la raíz (tatarabuelo/a): ")
            raiz = Nodo(nombre_raiz)
            print("Raíz creada con éxito.")
        else:
            print("La raíz ya ha sido creada.")
    
    elif opcion == "2":
        if raiz is None:
            print("Primero debes crear la raíz.")
        else:
            nombre_buscar = input("Ingresa el nombre del progenitor al que deseas agregar un hijo: ")
            cola = [raiz]
            encontrado = False

            while cola:
                actual = cola.pop(0)
                if actual.nombre == nombre_buscar:
                    nombre_hijo = input("Ingresa el nombre del hijo: ")
                    print(agregar_hijo(actual, nombre_hijo))
                    encontrado = True
                    break
                if actual.hijo_izquierdo:
                    cola.append(actual.hijo_izquierdo)
                if actual.hijo_derecho:
                    cola.append(actual.hijo_derecho)

            if not encontrado:
                print("Progenitor no encontrado.")
    
    elif opcion == "3":
        if raiz is None:
            print("El árbol está vacío.")
        else:
            mostrar_arbol(raiz)
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Intenta de nuevo.")
