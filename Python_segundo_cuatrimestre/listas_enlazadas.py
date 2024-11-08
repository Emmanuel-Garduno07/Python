class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class Lista:
    def __init__(self):
        self.head = None

    def final(self, dato):
        new_nodo = Nodo(dato)
        if self.head is None:
            self.head = new_nodo
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_nodo

    def imprimir_lista(self):
        last = self.head
        while last:
            print(last.dato, end=" -> ")
            last = last.next
        print("None")

if __name__ == "__main__":
    lista = Lista()
    lista.final(5)
    lista.final(9)
    lista.final(7)
    lista.final(8)
    lista.imprimir_lista()
