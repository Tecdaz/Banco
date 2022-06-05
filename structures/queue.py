from structures.node import Node

class Queue():
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    # Se usa para imprimir el mensaje de fila vacia cuando se haga mal uso de la misma
    __empty_queue = "Fila vacia"

    def append(self, data) -> None:
        '''Inserta un nuevo objeto de tipo cliente al final de la fila'''
        new_node = Node(data)

        # Recorre la fila hasta el final, si es el primer elemento lo inserta al principio
        if self.head == None:
            self.head = new_node
        else:
            iter = self.head
            while iter != None:
                iter = iter.next
            iter = new_node
        
        self.size += 1


    def empty_queue(self) -> bool:
        '''Retorna un valor booleano'''
        return self.size == 0


    def extract(self) -> Node:
        '''Extrae el nodo del principio y lo retorna para su uso posterior'''
        if self.empty_queue():
            print(self.__empty_queue)
        else:
            node_to_extract = self.head
            self.head = self.head.next
            node_to_extract.next = None
            self.size -= 1

        return node_to_extract


    def show_head(self) -> str:
        if self.empty_queue():
            return(self.__empty_queue)
        else:
            return str(self.head)
    