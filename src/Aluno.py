from Pessoa import Pessoa
from Responsavel import Responsavel

class Aluno(Pessoa):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__matricula = kwargs['matricula']
        self.__responsavel = kwargs['responsavel']

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, responsavel):
        self.__responsavel = responsavel