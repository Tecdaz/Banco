from services.console import clear
from objects.person import Person
from structures.priority_queue import Priority_queue
from structures.queue import Queue

main_queue = Queue()
extra_queues = []

def mesa_entrada():
    global extra_queues, main_queue
    new_client = Person()
    new_client.initialize()
    if len(extra_queues) == 0:
        main_queue.append(new_client)
    else:
        for queue in extra_queues:
            if new_client.is_client == queue.conditions["is_client"] and new_client.operation == queue.conditions["tramit"]:
                queue.append(new_client)
                return 0

        main_queue.append(new_client)

def new_queue():
    global extra_queues, main_queue

    def move_clients(is_client:bool, tramit:str, destiny:Priority_queue):
        global main_queue
        iter = main_queue.head
        aux_queue = Queue()
        while iter is not None:
            if iter.data.is_client == is_client and iter.data.operation == tramit:
                destiny.append(main_queue.extract())
            else:
                aux_queue.append(main_queue.extract())
            iter = iter.next
        main_queue = aux_queue

    
    if len(extra_queues) < 2:
        new_queue = Priority_queue()
        new_queue.set_conditions()
        extra_queues.append(new_queue)
        move_clients(new_queue.conditions['is_client'], new_queue.conditions["tramit"], new_queue)
    else:
        print('Ya alcanzo el numero maximo de filas especiales')

def view_main():
    clear()
    print(
'''Elija la accion que desea realizar:
1. Mesa de entrada
2. Atender proximo cliente
3. Abrir nueva cola
4. Cerrar cola especial
5. Listar operaciones
6. Salir

''')


if __name__ == '__main__':
    option = 0
    while option != 6:
        view_main()
        option = int(input("Seleccione una opcion: "))
        while option < 1 or option > 6:
            option = int(input("Seleccione una opcion valida: "))
        
        if option == 1:
            mesa_entrada()
        elif option == 3:
            new_queue()