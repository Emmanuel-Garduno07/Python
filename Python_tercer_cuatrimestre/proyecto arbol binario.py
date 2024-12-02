class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

class ArbolGenealogico:
    def __init__(self):
        self.raiz = None

    def establecer_raiz(self, nombre):
        if self.raiz is not None:
            print("El árbol ya tiene un progenitor principal.")
        else:
            self.raiz = Nodo(nombre)
            print("Progenitor principal agregado:", nombre)

    def agregar_hijo(self, nombre_padre, nombre_hijo):
        if self.raiz is None:
            print("El árbol aún no tiene un progenitor principal. No se puede agregar hijos.")
            return

        def buscar_y_agregar(nodo, nombre_padre, nombre_hijo):
            if nodo.nombre == nombre_padre:
                nodo.hijos.append(Nodo(nombre_hijo))
                print(f"Hijo '{nombre_hijo}' agregado a '{nombre_padre}'.")
                return True
            for hijo in nodo.hijos:
                if buscar_y_agregar(hijo, nombre_padre, nombre_hijo):
                    return True
            return False

        if not buscar_y_agregar(self.raiz, nombre_padre, nombre_hijo):
            print(f"No se encontró a '{nombre_padre}' en el árbol.")

    def verificar_persona(self, nombre):
        if self.raiz is None:
            print("El árbol aún no tiene un progenitor principal.")
            return False

        def buscar_persona(nodo, nombre):
            if nodo.nombre == nombre:
                return True
            for hijo in nodo.hijos:
                if buscar_persona(hijo, nombre):
                    return True
            return False

        if buscar_persona(self.raiz, nombre):
            print(f"La persona '{nombre}' existe en el árbol.")
            return True
        else:
            print(f"La persona '{nombre}' no existe en el árbol.")
            return False

    def mostrar_arbol(self):
        if self.raiz is None:
            print("El árbol aún no tiene un progenitor principal.")
            return

        def imprimir_arbol(nodo, nivel=0):
            print("  " * nivel + "- " + nodo.nombre)
            for hijo in nodo.hijos:
                imprimir_arbol(hijo, nivel + 1)

        imprimir_arbol(self.raiz)

# Programa principal con menú interactivo
arbol = ArbolGenealogico()

while True:
    print("\n--- Menú Árbol Genealógico ---")
    print("1. Establecer progenitor principal (raíz)")
    print("2. Agregar hijo a una persona")
    print("3. Verificar si una persona existe en el árbol")
    print("4. Mostrar árbol genealógico")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre_raiz = input("Ingrese el nombre del progenitor principal: ")
        arbol.establecer_raiz(nombre_raiz)
    elif opcion == "2":
        nombre_padre = input("Ingrese el nombre del padre/madre: ")
        nombre_hijo = input("Ingrese el nombre del hijo/a: ")
        arbol.agregar_hijo(nombre_padre, nombre_hijo)
    elif opcion == "3":
        nombre = input("Ingrese el nombre de la persona a verificar: ")
        arbol.verificar_persona(nombre)
    elif opcion == "4":
        print("\nÁrbol genealógico:")
        arbol.mostrar_arbol()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
