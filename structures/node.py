from objects.person import Person


class Node():
    def __init__(self, data: Person, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        '''Retorna en forma de string lo que contiene data'''
        return str(self.data)
