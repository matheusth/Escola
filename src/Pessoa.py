from abc import ABC, abstractclassmethod
class Pessoa(ABC):
    def __init__(self, **kwargs):
        self.__nome = kwargs['nome']
        self.__endereco = kwargs['endereco']
        self.__email = kwargs['email']

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
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