from Pessoa import Pessoa

class Responsavel(Pessoa):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__id = kwargs['id']
        self.__telefone = kwargs['telefone']

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
