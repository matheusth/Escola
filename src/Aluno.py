from Pessoa import Pessoa
from Responsavel import Responsavel

class Aluno(Pessoa):

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.__matricula = kwargs['matricula']
        self.__endereco = kwargs['endereco']
        self.__email = kwargs['email']
        self.__responsavel.append(kwargs['responsavel'])

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def responsavel(self):
        for i in self.__responsavel:
          print(self.__responsavel[i])

    @responsavel.setter
    def responsavel(self, responsavel):
        self.__responsavel.append(responsavel)