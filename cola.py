class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

    def __str__(self):
        return f"{self.valor}"


class Cola:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def pop_left(self):
        if not self.head:
            raise IndexError("No hay elementos en la cola")
        head = self.head
        self.head = self.head.next
        self.size -= 1
        if not self.head:
            self.tail = None
        return head

    def __str__(self):
        elementos = []
        actual = self.head
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.next
        return "[" + ", ".join(elementos) + "]"

    def add(self, valor):
        self.size += 1
        nuevo_nodo = Nodo(valor)
        if not self.head:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            self.tail = nuevo_nodo

    def size(self):
        return self.size
