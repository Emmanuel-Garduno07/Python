while True:
    print("\n--- Menú de Opciones ---")
    print("1. Contar números repetidos")
    print("2. Eliminar números repetidos")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    if opcion == '1':
        # Programa para contar números repetidos
        numeros = input("Ingresa números separados por espacios: ").split()
        numeros = [float(num) for num in numeros]

        for i in range(len(numeros)):
            contador = 0
            for j in range(len(numeros)):
                if numeros[i] == numeros[j]:
                    contador += 1
            if contador > 1:
                print(f"El número {numeros[i]} se repitió {contador} veces.")
                break
        else:
            print("No hay números repetidos.")

    elif opcion == '2':
        # Programa para eliminar números repetidos
        numeros = input("Ingresa números separados por espacios: ").split()
        numeros = [float(num) for num in numeros]
        resultado = []

        for num in numeros:
            if num not in resultado:
                resultado.append(num)

        print("Lista sin números repetidos:", resultado)

    elif opcion == '3':
        print("Saliendo del programa. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")
