from services.console import clear, select_options
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
        self.operation = select_options('Ingrese su operacion', operations)
        self.destinatary = select_options('Ingrese su destinatario', destinataries)
        self.amount = int(self.__input_data('Ingrese el monto'))
        self.is_client = bool(select_options('Es cliente?', is_client))

