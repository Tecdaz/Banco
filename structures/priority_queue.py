from services.console import select_options
from structures.queue import Queue
from services.bank import is_client, operations


class Priority_queue(Queue):
    def __init__(self) -> None:
        super().__init__()
        self.conditions = {'is_client': None, 'tramit': None}

    def set_conditions(self):
        '''Define las condiciones y las guarda en un diccionario'''

        self.conditions["is_client"] = select_options(
            "El ususario debe ser cliente?", is_client)
        self.conditions["tramit"] = select_options(
            "Seleccione el tipo de tramite", operations)
