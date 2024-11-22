class Nodo:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.siguiente = None

class Inventario:
    def __init__(self):
        self.cabeza = None

    def agregar_producto(self, codigo, nombre, cantidad, precio):
        nuevo = Nodo(codigo, nombre, cantidad, precio)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar_producto(self, codigo):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.codigo == codigo:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar_producto(self, codigo):
        actual = self.cabeza
        while actual:
            if actual.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None

    def modificar_producto(self, codigo, nuevo_nombre=None, nueva_cantidad=None, nuevo_precio=None):
        prod = self.buscar_producto(codigo)
        if prod:
            if nuevo_nombre:
                prod.nombre = nuevo_nombre
            if nueva_cantidad is not None:
                prod.cantidad = nueva_cantidad
            if nuevo_precio is not None:
                prod.precio = nuevo_precio
            return True
        return False

    def listar_productos(self):
        actual = self.cabeza
        if not actual:
            print("El inventario está vacío.")
            return
        while actual:
            print("Código:", actual.codigo, "| Nombre:", actual.nombre, "| Cantidad:", actual.cantidad, "| Precio:", actual.precio)
            actual = actual.siguiente

    def vaciar_inventario(self):
        self.cabeza = None
        print("Inventario vaciado.")

def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Buscar Producto")
        print("4. Listar Productos")
        print("5. Modificar Producto")
        print("6. Vaciar Inventario")
        print("7. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(codigo, nombre, cantidad, precio)
            print("Producto agregado.")

        elif opcion == "2":
            codigo = input("Código del producto a eliminar: ")
            if inventario.eliminar_producto(codigo):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            codigo = input("Código del producto a buscar: ")
            prod = inventario.buscar_producto(codigo)
            if prod:
                print("Encontrado - Código:", prod.codigo, "Nombre:", prod.nombre, "Cantidad:", prod.cantidad, "Precio:", prod.precio)
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            print("\nLista de productos:")
            inventario.listar_productos()

        elif opcion == "5":
            codigo = input("Código del producto a modificar: ")
            nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
            nueva_cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            nuevo_precio = input("Nuevo precio (dejar vacío para no cambiar): ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            if inventario.modificar_producto(codigo, nuevo_nombre, nueva_cantidad, nuevo_precio):
                print("Producto modificado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "6":
            inventario.vaciar_inventario()

        elif opcion == "7":
            print("Adiós.")
            break

        else:
            print("Opción no válida.")

menu()
