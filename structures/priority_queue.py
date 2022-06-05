from services.console import select_options
from structures.queue import Queue
from services.bank import is_client, operations

class Priority_queue(Queue):
    def __init__(self) -> None:
        super().__init__()
        self.conditions = []

    def set_conditions(self):
        self.conditions.append(bool(
            select_options("El ususario debe ser cliente?", is_client)
            ))
        self.conditions.append(select_options("Seleccione el tipo de tramite", operations))