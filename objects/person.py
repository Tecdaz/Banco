from turtle import st
from services.console import clear
from services.bank import operations, destinataries, is_client


class Person():
    def __init__(self) -> None:
        self.name: str = None
        self.age: int = None
        self.operation: str = None
        self.destinatary: str = None
        self.amount: int = None
        self.is_client: bool = None

    # Private

    def __select_options(self, message, options) -> str:
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

    def __input_data(self, message) -> str:
        '''
        Retorna cadenas no vacias
        '''
        clear()
        data = input(message+': ')
        while len(data) == 0:
            data = input(message+' valid@:')

        return data

    def __str__(self) -> str:
        '''Es lo que retorna cada que se invoca el modelo desde la funcion print'''

        return f'''
Nombre: {self.name}
Edad: {self.age}
Operacion: {self.operation}
Destinatario: {self.destinatary}
Monto: {self.amount}
{"Es cliente" if self.is_client else "No es cliente"}'''

    # Public

    def initialize(self):
        '''Solicita datos para la persona'''
        self.name = self.__input_data("Ingrese el nombre")
        self.age = int(self.__input_data('Ingrese la edad'))
        self.operation = self.__select_options('Ingrese su operacion', operations)
        self.destinatary = self.__select_options('Ingrese su destinatario', destinataries)
        self.amount = int(self.__input_data('Ingrese el monto'))
        self.is_client = bool(self.__select_options('Es cliente?', is_client))

