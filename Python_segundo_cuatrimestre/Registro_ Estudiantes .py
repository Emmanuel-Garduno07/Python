programacion = set()
redes = set()


def mostrar_opciones():
    print("\nOpciones:")
    print("1. Agregar estudiante a Programación")
    print("2. Agregar estudiante a Redes")
    print("3. Mostrar estudiantes inscritos")
    print("4. Salir")

while True:
    mostrar_opciones()
    opcion = input("Selecciona una opción (1-4): ").strip()

    if opcion == '1':
        nombre = input("Ingresa el nombre del estudiante para Programación: ").strip()
        programacion.add(nombre)
        print(f"'{nombre}' ha sido agregado a Programación.")
    elif opcion == '2':
        nombre = input("Ingresa el nombre del estudiante para Redes: ").strip()
        redes.add(nombre)
        print(f"'{nombre}' ha sido agregado a Redes.")
    elif opcion == '3':
        print("\n--- Estudiantes Inscritos ---")
        print("Programación:", sorted(programacion) if programacion else "Ninguno")
        print("Redes:", sorted(redes) if redes else "Ninguno")
    elif opcion == '4':
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida (1-4).")
