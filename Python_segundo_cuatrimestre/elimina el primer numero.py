numeros = []
for i in range(1, 11):
    numeros.append(i)
print("Cantidad de números:", len(numeros))
print("Lista de números:", numeros)
while numeros:
    opcion = input("¿Deseas eliminar el primer número agregado? (s/n): ").lower()
    if opcion == 's':
        eliminado = numeros.pop(0)
        print("Número eliminado:", eliminado)
    else:
        print("No se eliminó ningún número.")
        break 
    print("Lista actualizada de números:", numeros)
if not numeros:
    print("La lista está vacía.")
