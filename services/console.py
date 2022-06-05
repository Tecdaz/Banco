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