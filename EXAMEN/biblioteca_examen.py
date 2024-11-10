usuarios = {}
libros_disponibles = ["El Quijote", "Cien años de soledad"]

# Cuenta del administrador
administrador = {"usuario": "admin", "contraseña": "admin123"}

def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    nombre = input("Ingrese su nombre: ")
    usuario = input("Cree un nombre de usuario: ")
    contraseña = input("Cree una contraseña: ")
    usuarios[usuario] = {"nombre": nombre, "contraseña": contraseña}
    print("¡Registro exitoso!\n")

def iniciar_sesion():
    print("\n--- Iniciar Sesión ---")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
   
    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        print("Inicio de sesión exitoso como usuario.")
        menu_usuario(usuario)

    elif usuario == administrador["usuario"] and contraseña == administrador["contraseña"]:
        print("Inicio de sesión exitoso como administrador.")
        menu_administrador()
    else:
        print("Usuario o contraseña incorrectos.\n")

def menu_principal():
    while True:
        print("\n--- Biblioteca CLI ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida.\n")

def menu_usuario(usuario):
    while True:
        print("\n--- Menú de Usuario ---")
        print("1. Ver libros disponibles")
        print("2. Pedir un libro")
        print("3. Devolver un libro")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("Libros disponibles:", libros_disponibles, "\n")
        elif opcion == "2":
            libro = input("Ingrese el nombre del libro que desea pedir: ")
            if libro in libros_disponibles:
                print("Has pedido el libro:", libro, "\n")
            else:
                print("El libro no está disponible.\n")
        elif opcion == "3":
            libro = input("Ingrese el nombre del libro que desea devolver: ")
            print("Has devuelto el libro:", libro, "\n")
        elif opcion == "4":
            print("Cerrando sesión de usuario.\n")
            break
        else:
            print("Opción no válida.\n")

def menu_administrador():
    while True:
        print("\n--- Menú del Administrador ---")
        print("1. Ver todos los usuarios registrados")
        print("2. Ver libros disponibles")
        print("3. Agregar libro")
        print("4. Eliminar libro")
        print("5. Cerrar sesión")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("Usuarios registrados:")
            for user in usuarios:
                print("Usuario:", user, "Nombre:", usuarios[user]["nombre"])
            print("\n")
        elif opcion == "2":
            print("Libros disponibles:", libros_disponibles, "\n")
        elif opcion == "3":
            libro = input("Ingrese el nombre del libro que desea agregar: ")
            if libro not in libros_disponibles:
                libros_disponibles.append(libro)
                print("Has agregado el libro:", libro, "\n")
            else:
                print("El libro ya está disponible.\n")
        elif opcion == "4":
            libro = input("Ingrese el nombre del libro que desea eliminar: ")
            if libro in libros_disponibles:
                libros_disponibles.remove(libro)
                print("Has eliminado el libro:", libro, "\n")
            else:
                print("El libro no se encuentra en la lista.\n")
        elif opcion == "5":
            print("Cerrando sesión del administrador.\n")
            break
        else:
            print("Opción no válida.\n")

menu_principal()
