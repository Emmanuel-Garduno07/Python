agregar_elemento = []

def imprimir_arreglo():
    print('Contenido del arreglo:', agregar_elemento)
    print('Cantidad de elementos en el arreglo:', len(agregar_elemento))
    if len(agregar_elemento) > 0:
        print('Último número ingresado:', agregar_elemento[-1])
    else:
        print('No hay números en el arreglo.')

while True:
    try:
       
        agregar_elemento.append(int(input('Ingresa un número: ')))
        imprimir_arreglo()  
    except ValueError:
        print('Entrada no válida. Por favor, ingresa un número.')
        continue 

    while len(agregar_elemento) > 0:
        opcion_eliminar = input('¿Quieres eliminar el último número? (s/n): ').lower()
        if opcion_eliminar == 's':
            eliminado = agregar_elemento.pop()
            print('Número ' + str(eliminado) + ' eliminado del arreglo.')
            imprimir_arreglo() 
            if len(agregar_elemento) == 0:
                print('El arreglo está vacío.')
                break  
            break  

    opcion_salir = input('¿Quieres salir? (s/n): ').lower()
    if opcion_salir == 's':
        break

imprimir_arreglo()
