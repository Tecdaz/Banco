import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def select_options(message, options) -> str:
    '''
    Despliega un menu de opciones que viene dado por la lista/tupla options
    Verifica que la opcion este en el rango de opciones disponibles
    Retorna la opcion escogida
    '''
    clear()
    print(message, end='\n')

    for index, item in enumerate(options):
        print(f'{index+1}. {item}')

    option = int(input("Seleccione una opcion: "))
    while option < 1 or option > len(options):
        option = int(input("Seleccione una opcion valida: "))

    return options[option-1]


def print_list(list):
    '''imprime una lista con sus elemento separados por comas'''
    result = ""
    for i in list:
        result += str(i)+', '
    return result[:-2]


def end_message(message):
    '''Muestra el mensaje final de cada operacion'''
    clear()
    input(message+' ->')
