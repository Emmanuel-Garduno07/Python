# Lista determinada
lista = [1, 3]

print("Lista original:", lista)

entrada = input("Ingresa números para agregar a la lista (separados por comas): ")

numeros = entrada.split(',')
for num in numeros:
    lista.append(int(num))

lista.sort()
print("Lista ordenada de menor a mayor:", lista)

lista.sort(reverse=True)
print("Lista ordenada de mayor a menor:", lista)

