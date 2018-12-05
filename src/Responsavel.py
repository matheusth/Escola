from src.Pessoa import Pessoa

class Responsavel(Pessoa):
    def __init__(self, **kwargs):
        self.__nome = kwargs['nome']
        self.__telefone = kwargs['telefone']

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
