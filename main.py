from services.console import clear, print_list, end_message
from objects.person import Person
from structures.priority_queue import Priority_queue
from structures.queue import Queue

main_queue = Queue()
extra_queues = []
operations_history = []


def mesa_entrada():
    '''Ingresa un nuevo cliente y lo inserta en la fila correspondiente'''
    global extra_queues, main_queue
    # Crea el cliente
    new_client = Person()
    new_client.initialize()

    if len(extra_queues) == 0:
        main_queue.append(new_client)
    else:
        # Recorre las filas especiales para saber en cual ingresar el cliente, usa un return forsozo para salir de la funcion
        for queue in extra_queues:
            if new_client.is_client == queue.conditions["is_client"] and new_client.operation == queue.conditions["tramit"]:
                queue.append(new_client)
                return None
        # Si no hace el return carga el cliente en la fila principal
        main_queue.append(new_client)
    end_message('Cliente creado con exito!!')


def attend_client():
    '''Muestra un menu con las filas disponibles para atender personas'''
    clear()

    def extract_client(queue):
        '''Extrae el cliente y guarda sus datos en la lista de operaciones'''
        global main_queue, extra_queues, operations_history
        if not queue.empty_queue():
            # Lo que hace es guardar en la lista el objeto Persona lista->nodo->data
            operations_history.append(queue.extract().data)
            end_message('Cliente atendido!')
        else:
            end_message('No hay clientes para atender')

    def select_queue():
        '''Menu para mostrar la lista de filas para atender, con la cantidad de clientes de las mismas'''

        print('Seleccione la fila que desea atender')
        # Siempre muestra la fila general
        print('1. Fila general. Clientes ', main_queue.size)
        # Imprime las filas especiales
        for index, queue in enumerate(extra_queues):
            print(index+2, '. ', print_list(queue.conditions.values()),
                  '. Clientes ', queue.size)
        # Selecciona una opcion valida
        option = int(input('Seleccione una fila: '))
        while option < 1 or option > len(extra_queues)+1:
            option = int(input('Seleccione una opcion correcta: '))

        if option == 1:
            extract_client(main_queue)
        else:
            extract_client(extra_queues[option-2])

    # Si no hay filas especiales directamente atiende de la fila general
    if len(extra_queues) == 0:
        extract_client(main_queue)
    else:
        select_queue()


def new_queue():
    '''Crea una nueva Fila pasando a las personas que pertenecen a ella'''
    global extra_queues, main_queue

    def move_clients(is_client, tramit, destiny: Priority_queue):
        '''Mueve los clientes atendiendo al criterio combinado'''
        global main_queue
        # Fila auxiliar para ingresar los que no cumplan la condicion
        aux_queue = Queue()
        # Vacia la fila principal
        while not main_queue.empty_queue():
            if main_queue.head.data.is_client == is_client and main_queue.head.data.operation == tramit:
                destiny.append(main_queue.extract())
            else:
                aux_queue.append(main_queue.extract())
        # Llena la fila principal con los usuarios que no se van a cambiar de fila
        while not aux_queue.empty_queue():
            main_queue.append(aux_queue.extract())

    if len(extra_queues) < 2:
        # Crea la fila y la agrega a la lista de listas especiales
        new_queue = Priority_queue()
        new_queue.set_conditions()
        extra_queues.append(new_queue)

        move_clients(
            new_queue.conditions['is_client'], new_queue.conditions["tramit"], new_queue)
        end_message('Fila creada con exito!!')
    else:
        end_message('Ya alcanzo el numero maximo de filas especiales.')


def close_queue():
    '''Cierra solo las filas especiales vacias'''
    global extra_queues
    clear()

    def avalible_queues(queues_list):
        '''Retorna el numero de filas disponibles para cerrar'''
        result = 0
        for queue in queues_list:
            if queue.empty_queue():
                result += 1
        return result

    if avalible_queues(extra_queues) > 0:
        print('Fila/s disponible/s para cerrar')
        # Diccionario para guardar la fila de acuerdo a su posicion, asi se accede a ella mediante una llave
        options = {}
        iter = 1
        # Muestra unicamente filas vacias
        for queue in extra_queues:
            if queue.empty_queue():
                print(iter, '. ',  print_list(queue.conditions.values()))
                options[iter] = queue
                iter += 1

        option_selected = int(input('Seleccione que fila desea cerrar: '))
        while option_selected < 1 or option_selected > iter:
            option_selected = int(input('Ingrese una opcion valida: '))

        extra_queues.remove(options[option_selected])
        end_message('Fila cerrada!')
    else:
        end_message('No hay filas especiales abiertas')


def list_operations():
    '''Lista las operaciones que cumplan con las condiciones'''
    clear()
    min = int(input('Monto minimo: '))
    max = int(input('Monto maximo: '))
    count = 1
    for person in operations_history:
        if person.amount >= min and person.amount <= max:
            print('\n', count, '.')
            print(person)
            count += 1
    input('\nPresione una tecla para volver ->')


def view_main():
    '''Vista principal de la aplicacion'''
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
        elif option == 2:
            attend_client()
        elif option == 3:
            new_queue()
        elif option == 4:
            close_queue()
        elif option == 5:
            list_operations()
